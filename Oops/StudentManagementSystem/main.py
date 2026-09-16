from StudentManagementSystem import Student 
from log import logger

if __name__ == "__main__":
    print("Starting Student Management System...")

    try:
        # Creating valid student objects
        student1 = Student("Aarav Sharma", "aarav@email.com", "S101", "Computer Science", [85, 90, 78])
        student2 = Student("Diya Patel", "diya@email.com", "S102", "Mathematics", [92, 88, 95])

        # Display details
        student1.display_details()
        student2.display_details()

        # Update marks successfully
        student1.update_marks([88, 91, 80])
        student1.display_details()

        # Test Exception Handling with invalid marks (> 100)
        print("\nTesting exception handling for invalid marks...")
        student2.update_marks([105, 50, 60])

        # Display total number of students via class method
        print(f"\nTotal Number of Students: {Student.get_total_students()}")

    except Exception as ex:
        logger.critical(f"An unexpected error occurred: {ex}")
        print(f"Critical Error: {ex}")