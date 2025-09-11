import inspect
import enrollment

def test_add_student_query():
    db = enrollment.StudentCourseDB()
    expected_query = "INSERT INTO students (name, email) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_student)
    assert expected_query in actual_query

def test_add_course_query():
    db = enrollment.StudentCourseDB()
    expected_query = "INSERT INTO courses (course_name, credits) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_course)
    assert expected_query in actual_query

def test_enroll_student_query():
    db = enrollment.StudentCourseDB()
    expected_query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(db.enroll_student)
    assert expected_query in actual_query

def test_list_student_courses_query():
    db = enrollment.StudentCourseDB()
    expected_query = "SELECT c.course_name, c.credits, e.enrollment_date"
    actual_query = inspect.getsource(db.list_student_courses)
    assert expected_query in actual_query

def test_course_wise_report_query():
    db = enrollment.StudentCourseDB()
    expected_query = "SELECT s.student_id, s.name, s.email, e.enrollment_date"
    actual_query = inspect.getsource(db.course_wise_report)
    assert expected_query in actual_query

# --- Method signature tests ---

def test_add_student_signature():
    sig = inspect.signature(enrollment.StudentCourseDB.add_student)
    assert list(sig.parameters.keys()) == ["self", "name", "email"]

def test_add_course_signature():
    sig = inspect.signature(enrollment.StudentCourseDB.add_course)
    assert list(sig.parameters.keys()) == ["self", "course_name", "credits"]

def test_enroll_student_signature():
    sig = inspect.signature(enrollment.StudentCourseDB.enroll_student)
    assert list(sig.parameters.keys()) == ["self", "student_id", "course_id", "enrollment_date"]

def test_list_student_courses_signature():
    sig = inspect.signature(enrollment.StudentCourseDB.list_student_courses)
    assert list(sig.parameters.keys()) == ["self", "student_id"]

def test_course_wise_report_signature():
    sig = inspect.signature(enrollment.StudentCourseDB.course_wise_report)
    assert list(sig.parameters.keys()) == ["self", "course_id"]
