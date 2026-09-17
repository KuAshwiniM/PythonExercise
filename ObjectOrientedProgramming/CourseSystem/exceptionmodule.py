class CoursePlatformError(Exception):
    """Base exception class for the online learning platform."""
    pass

class InvalidCourseDataError(Exception):
    """Exception raised when provided course parameters are invalid."""
    pass