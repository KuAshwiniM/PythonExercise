from loggingmodule import logger
from exceptionmodule import CoursePlatformError, InvalidCourseDataError
from course import Course, PremiumCourse

def course_platform_demo():
    logger.info("Initializing Online Learning Platform Testing Routine...")

    try:
        # 1. Spawn a standard course instance
        python_basics = Course(
            course_name="Python Automation Foundations", 
            instructor="Al Sweigart", 
            duration=35, 
            price=49.99
        )
        python_basics.show_course_details()
        
        # Test baseline methods
        discounted_price = python_basics.calculate_discount(15)
        print(f"Promo Alert! 15% discount applied price: ${discounted_price:.2f}")

        # 2. Spawn a child Premium course instance
        ml_bootcamp = PremiumCourse(
            course_name="Machine Learning & Deep Learning Masterclass",
            instructor="Dr. Angela Yu",
            duration=120,
            price=299.99,
            mentor_support=True,
            live_sessions=24
        )
        ml_bootcamp.show_course_details()
        
        # Verify inherited parent operations execution on child tiers
        premium_discounted = ml_bootcamp.calculate_discount(20)
        print(f"VIP Holiday Special! 20% discount applied premium price: ${premium_discounted:.2f}")

        # 3. Request class diagnostic metric using class method execution
        total_created = Course.get_course_count()
        print(f"\n[Platform Metrics] Current total registered items: {total_created}")

        # 4. Intentionally provoke error routines to demonstrate exception fallback
        logger.info("Testing data validation layers with faulty parameters...")
        faulty_course = Course("Broken Course Track", "Ghost Writer", -5, 10.00)

    except CoursePlatformError as cpe:
        logger.error(f"Application caught an explicit constraint breach: {cpe}")
    except Exception as general_err:
        logger.critical(f"An unexpected system exception triggered: {general_err}")

if __name__ == "__main__":
    course_platform_demo()