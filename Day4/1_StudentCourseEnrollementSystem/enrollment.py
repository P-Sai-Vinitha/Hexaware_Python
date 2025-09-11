from config import get_connection
from mysql.connector import Error

class StudentCourseDB:
    def add_student(self, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            print(f"Student {name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_course(self, course_name, credits):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO courses (course_name, credits) VALUES (%s, %s)",
                (course_name, credits)
            )
            conn.commit()
            print(f"Course {course_name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def enroll_student(self, student_id, course_id, enrollment_date):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            # prevent duplicate enrollment
            cursor.execute(
                "SELECT * FROM enrollments WHERE student_id = %s AND course_id = %s",
                (student_id, course_id)
            )
            if cursor.fetchone():
                print("Error: Student already enrolled in this course.")
                return
            
            cursor.execute(
                "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
                (student_id, course_id, enrollment_date)
            )
            conn.commit()
            print(f"Student {student_id} enrolled in course {course_id}.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_student_courses(self, student_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.course_name, c.credits, e.enrollment_date
                FROM enrollments e
                JOIN courses c ON e.course_id = c.course_id
                WHERE e.student_id = %s
            """, (student_id,))
            rows = cursor.fetchall()
            print(f"Courses for Student {student_id}:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def course_wise_report(self, course_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.student_id, s.name, s.email, e.enrollment_date
                FROM enrollments e
                JOIN students s ON e.student_id = s.student_id
                WHERE e.course_id = %s
            """, (course_id,))
            rows = cursor.fetchall()
            print(f"Students in Course {course_id}:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
