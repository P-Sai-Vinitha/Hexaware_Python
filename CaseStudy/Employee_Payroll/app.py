from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config import Config
import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

# -------------------------------
# Database Models
# -------------------------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum("Admin", "Employee"), nullable=False)

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50))
    salary = db.Column(db.Numeric(10, 2))
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))

# -------------------------------
# Authentication Route
# -------------------------------
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:  # Replace with hash check in production
        #token = create_access_token(identity={"id": user.id, "role": user.role})
        token = create_access_token(identity=json.dumps({"id": user.id, "role": user.role}))

        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

# -------------------------------
# Department Routes
# -------------------------------
@app.route("/departments", methods=["POST"])
@jwt_required()
def add_department():
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())

    if user["role"] != "Admin":
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json()
    dept = Department(name=data["name"], manager_id=data["manager_id"])
    db.session.add(dept)
    db.session.commit()
    return jsonify({"message": "Department added", "id": dept.id})

@app.route("/departments", methods=["GET"])
@jwt_required()
def list_departments():
    depts = Department.query.all()
    return jsonify([{"id": d.id, "name": d.name} for d in depts])

# -------------------------------
# Employee Routes
# -------------------------------
@app.route("/employees", methods=["POST"])
@jwt_required()
def add_employee():
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())
    if user["role"] != "Admin":
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json()
    emp = Employee(
        name=data["name"],
        position=data["position"],
        salary=data["salary"],
        department_id=data["department_id"],
        created_by=user["id"]
    )
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added", "id": emp.id})

@app.route("/employees/<int:id>", methods=["PUT"])
@jwt_required()
def update_salary(id):
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())
    if user["role"] != "Admin":
        return jsonify({"error": "Unauthorized"}), 403
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    emp.salary = data["salary"]
    emp.updated_by = user["id"]
    db.session.commit()
    return jsonify({"message": "Salary updated"})

@app.route("/employees", methods=["GET"])
@jwt_required()
def list_employees():
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())
    if user["role"] != "Admin":
        return jsonify({"error": "Unauthorized"}), 403
    emps = Employee.query.all()
    return jsonify([{"id": e.id, "name": e.name, "salary": float(e.salary)} for e in emps])

@app.route("/employees/<int:id>", methods=["GET"])
@jwt_required()
def view_employee(id):
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Not found"}), 404
    if user["role"] == "Employee" and user["id"] != id:
        return jsonify({"error": "Unauthorized"}), 403
    return jsonify({
        "name": emp.name,
        "position": emp.position,
        "salary": float(emp.salary)
    })

@app.route("/employees/salary", methods=["GET"])
@jwt_required()
def filter_salary():
    #user = get_jwt_identity()
    user = json.loads(get_jwt_identity())
    if user["role"] != "Admin":
        return jsonify({"error": "Unauthorized"}), 403
    min_salary = request.args.get("min", type=float)
    max_salary = request.args.get("max", type=float)
    query = Employee.query
    if min_salary is not None:
        query = query.filter(Employee.salary >= min_salary)
    if max_salary is not None:
        query = query.filter(Employee.salary <= max_salary)
    emps = query.all()
    return jsonify([{"id": e.id, "name": e.name, "salary": float(e.salary)} for e in emps])

# -------------------------------
# App Initialization
# -------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
