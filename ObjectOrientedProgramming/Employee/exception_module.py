class InvalidSalaryError(Exception):
    """Raised when salary is negative or non-numeric."""
    pass

class InvalidIDError(Exception):
    """Raised when employee ID is invalid."""
    pass