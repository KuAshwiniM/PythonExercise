from exception_module import InvalidSalaryError, InvalidIDError

class Employee:
    """Base class representing a general employee."""
    def __init__(self, emp_id, name, salary, department):
        if not emp_id:
            raise InvalidIDError("Employee ID cannot be empty.")
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
            
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        """Displays base employee details."""
        print(f"ID: {self.emp_id} | Name: {self.name} | Department: {self.department} | Salary: ${self.salary:,.2f}")


class Developer(Employee):
    """Child class inheriting from Employee, specific to Developers."""
    def __init__(self, emp_id, name, salary, department, programming_language, experience_years):
        super().__init__(emp_id, name, salary, department)
        self.programming_language = programming_language
        self.experience_years = experience_years

    def display_details(self):
        """Overrides/extends display_details to show developer-specific info while leveraging parent data conceptually."""
        # Accessing base/parent representation or fields directly via inheritance
        super().display_details()
        print(f"   ↳ Language: {self.programming_language} | Experience: {self.experience_years} years")