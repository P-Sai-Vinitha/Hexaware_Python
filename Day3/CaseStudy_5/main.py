from course import Course
from student import Student
from premium_student import PremiumStudent

# Create courses
python_course = Course("Python Programming", "PY101", 3, 500)
data_science = Course("Data Science 101", "DS101", 4, 700)
ml_course = Course("Machine Learning", "ML201", 5, 1000)

# Create students
alice = Student("Neethu")
bob = PremiumStudent("Vinitha")

# Neethu's enrollment
alice.enrollment.enroll_course(python_course)
alice.enrollment.enroll_course(data_science)
alice.enrollment.enroll_course(ml_course)
alice.enrollment.display_enrollment()
alice.display_totals()

print("\n---\n")

# another enrollment
bob.enrollment.enroll_course(python_course)
bob.enrollment.enroll_course(data_science)
bob.enrollment.enroll_course(ml_course)
bob.enrollment.drop_course("DS101")
bob.enrollment.display_enrollment()
bob.display_totals()
