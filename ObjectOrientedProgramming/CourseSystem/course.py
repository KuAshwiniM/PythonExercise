from loggingmodule import logger
from exceptionmodule import CoursePlatformError, InvalidCourseDataError

class Course:
    # Class variable tracking total courses built across the platform
    _course_count = 0

    def __init__(self, course_name: str, instructor: str, duration: int, price: float):
        """
        Initializes a standard platform course.
        :param duration: Time duration in hours
        :param price: Retail value of the course
        """
        if not course_name or not instructor:
            raise InvalidCourseDataError("Course name and instructor cannot be empty values.")
        if duration <= 0 or price < 0:
            raise InvalidCourseDataError("Duration must be positive and price cannot be negative.")

        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        # Increment class level registry counter
        Course._course_count += 1
        logger.info(f"Successfully created base course: '{self.course_name}'")

    @classmethod
    def get_course_count(cls) -> int:
        """Class method returning the total registered courses."""
        return cls._course_count

    def calculate_discount(self, discount_percentage: float) -> float:
        """Calculates and returns a promotional price based on an input percentage."""
        if not (0 <= discount_percentage <= 100):
            raise InvalidCourseDataError("Discount percentage must sit between 0 and 100.")
        return self.price * (1 - (discount_percentage / 100))

    def show_course_details(self) -> None:
        """Prints out the complete descriptive breakdown of a core course."""
        print(f"\n--- Course Details: {self.course_name} ---")
        print(f"Instructor: {self.instructor}")
        print(f"Duration  : {self.duration} Hours")
        print(f"Base Price: ${self.price:.2f}")


class PremiumCourse(Course):
    """Derived class extending Course with interactive and localized attributes."""
    
    def __init__(self, course_name: str, instructor: str, duration: int, price: float, 
                 mentor_support: bool, live_sessions: int):
        """
        Initializes a specialized Premium tier course.
        :param mentor_support: Boolean representing direct access to mentors
        :param live_sessions: Count of live interaction calls bundled with the curriculum
        """
        # Call base class constructor to build shared state attributes
        super().__init__(course_name, instructor, duration, price)
        
        if live_sessions < 0:
            raise InvalidCourseDataError("Live session count cannot be a negative value.")
            
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions
        logger.info(f"Upgraded properties added to Premium course: '{self.course_name}'")

    def show_course_details(self) -> None:
        """Overrides parent method to introduce supplementary Premium metadata details."""
        super().show_course_details()
        print(f"Premium Tier Add-ons:")
        print(f" -> Dedicated Mentor Support: {'Available' if self.mentor_support else 'Unavailable'}")
        print(f" -> Live Sync Sessions     : {self.live_sessions} Scheduled Sessions")