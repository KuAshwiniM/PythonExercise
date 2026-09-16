from employee_module import Employee, Developer
from exception_module import InvalidSalaryError, InvalidIDError
from logging_module import logger

def main():
    logger.info("Application started.")

    try:
        # Creating at least 3 Employee/Developer objects
        dev1 = Developer("E101", "Alice Smith", 85000, "Engineering", "Python", 4)
        dev2 = Developer("E102", "Bob Jones", 95000, "Engineering", "JavaScript", 6)
        emp1 = Employee("E103", "Charlie Davis", 50000, "Human Resources")

        print("--- Employee & Developer Records ---")
        dev1.display_details()
        print("-" * 40)
        dev2.display_details()
        print("-" * 40)
        emp1.display_details()  # Demonstrating parent functionality directly

        logger.info("Successfully displayed details for 3 objects.")

        # Triggering custom exception test safely
        print("\n--- Testing Exception Handling ---")
        invalid_dev = Developer("E104", "David", -5000, "Engineering", "C++", 2)

    except (InvalidSalaryError, InvalidIDError) as e:
        print(f"Validation Error Caught: {e}")
        logger.error(f"Validation error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logger.critical(f"Critical error: {e}")

if __name__ == "__main__":
    main()