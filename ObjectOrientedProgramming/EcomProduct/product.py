from  loggingmodule import logger
from exceptionmodule import InsufficientStockError, InvalidQuantityError


class Product:
    def __init__(self, product_id: str, name: str, price: float,
                 category: str, stock_quantity: int):
        if not self.is_valid_price(price):
            raise ValueError(f"Initialization failed: Price must be greater than zero. Got {price}")
        if stock_quantity < 0:
            raise ValueError(f"Initialization failed: Stock cannot be negative. Got {stock_quantity}")
            
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        logger.debug(f"Product '{self.name}' (ID: {self.product_id}) initialized successfully.")

    @staticmethod
    def is_valid_price(price: float) -> bool:
        """Validates if the product price is greater than zero."""
        return isinstance(price, (int, float)) and price > 0

    def display_product(self) -> None:
        """Prints the product details to the console."""
        info = (
            f"--- Product Info ---\n"
            f"ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: ${self.price:.2f}\n"
            f"Available Stock: {self.stock_quantity}\n"
            f"--------------------"
        )
        print(info)

    def update_stock(self, quantity: int) -> None:
        """Updates the stock quantity. Supports positive restocks and negative deductions."""
        new_stock = self.stock_quantity + quantity
        if new_stock < 0:
            logger.error(f"Failed to update stock for {self.name}. Resulting stock would be negative ({new_stock}).")
            raise InsufficientStockError(f"Cannot deduct {abs(quantity)} units. Only {self.stock_quantity} available.")
        
        self.stock_quantity = new_stock
        logger.info(f"Stock updated for '{self.name}' by {quantity:+} units. Current stock: {self.stock_quantity}.")

    def calculate_total_price(self, quantity: int) -> float:
        """Calculates the total cost for a specified quantity of the product."""
        if quantity <= 0:
            logger.error(f"Invalid quantity requested for price calculation: {quantity}")
            raise InvalidQuantityError("Quantity for price calculation must be greater than zero.")
        
        total = self.price * quantity
        logger.debug(f"Calculated total for {quantity}x '{self.name}': ${total:.2f}")
        return total