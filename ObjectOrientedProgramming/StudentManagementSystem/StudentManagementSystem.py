from log import logger
from exceptionhandling import InvalidMarksError

class Student:
    # Class variable to track total number of students
    total_students = 0

    def __init__(self, name, email, student_id, course, marks):
        """Initialize student attributes and validate marks."""
        try:
            self.name = name
            self.email = email
            self.student_id = student_id
            self.course = course

            # Validate and set marks
            self.marks = self._validate_marks(marks)

            # Increment total student count
            Student.total_students += 1
            logger.info(f"Student created successfully: {self.name} (ID: {self.student_id})")
        except (TypeError, InvalidMarksError) as e:
            logger.error(f"Failed to create student {name} (ID: {student_id}): {e}")
            raise

    @staticmethod
    def _validate_marks(marks):
        """Helper method to ensure marks are in a list/dict and within 0-100."""
        if not isinstance(marks, list):
            raise TypeError("Marks must be provided as a list of numbers.")
        for mark in marks:
            if not (0 <= mark <= 100):
                raise InvalidMarksError(f"Mark {mark} is invalid. Must be between 0 and 100.")
        return marks

    def display_details(self):
        """Display individual student information."""
        avg = self.calculate_average()
        print(f"\n--- Student Details ---")
        print(f"ID     : {self.student_id}")
        print(f"Name   : {self.name}")
        print(f"Email  : {self.email}")
        print(f"Course : {self.course}")
        print(f"Marks  : {self.marks}")
        print(f"Average: {avg:.2f}")

    def update_marks(self, new_marks):
        """Update existing marks with validation and exception handling."""
        try:
            validated_marks = self._validate_marks(new_marks)
            self.marks = validated_marks
            logger.info(f"Marks updated for student ID {self.student_id}")
            print(f"Marks successfully updated for {self.name}!")
        except (TypeError, InvalidMarksError) as e:
            logger.error(f"Failed to update marks for ID {self.student_id}: {e}")
            print(f"Error updating marks: {e}")

    def calculate_average(self):
        """Calculate and return the average of the student's marks."""
        if len(self.marks) == 0:
            return 0.0
        return sum(self.marks) / len(self.marks)

    @classmethod
    def get_total_students(cls):
        """Class method to return the total number of student objects created."""
        return cls.total_students