class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the current balance."""
    pass

class InvalidAmountError(Exception):
    """Raised when a negative or zero amount is provided for deposit/withdrawal."""
    pass