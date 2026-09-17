class InsufficientStockError(Exception):
    """Raised when a purchase quantity exceeds available stock."""
    pass

class InvalidQuantityError(Exception):
    """Raised when an operation receives a negative or zero quantity."""
    pass