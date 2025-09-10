class Enrollment:
    def __init__(self):
        self.courses = []
        self.last_enrolled_course = None  # Dynamic attribute

    def enroll_course(self, course):
        if course in self.courses:
            print(f"Already enrolled in '{course.name}'.")
        else:
            self.courses.append(course)
            self.last_enrolled_course = course.name
            print(f"Enrolled '{course.name}' successfully.")

    def drop_course(self, course_code):
        for course in self.courses:
            if course.code == course_code:
                self.courses.remove(course)
                print(f"Dropped '{course.name}' successfully.")
                return
        print(f"Course with code '{course_code}' not found in your enrolled list.")

    def calculate_total_credits(self):
        return sum(course.credits for course in self.courses)

    def calculate_total_fees(self):
        return sum(course.get_fee() for course in self.courses)

    def display_enrollment(self):
        if not self.courses:
            print("No courses enrolled.")
            return
        print("Enrolled Courses:")
        for course in self.courses:
            print(f"- {course.name} ({course.code}) - Credits: {course.credits}, Fee: ₹{course.get_fee()}")
        print(f"Total Credits: {self.calculate_total_credits()} | Total Fees: ₹{self.calculate_total_fees()}")
