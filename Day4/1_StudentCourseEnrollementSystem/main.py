from enrollment import StudentCourseDB

db = StudentCourseDB()

db.add_student("Neethu", "neethu@example.com")
db.add_student("Vinitha", "vinitha@example.com")

db.add_course("Python Programming", 4)
db.add_course("Data Structures", 3)

db.enroll_student(1, 1, "2025-09-11")
db.enroll_student(1, 2, "2025-09-11")

db.list_student_courses(1)

db.course_wise_report(1)
