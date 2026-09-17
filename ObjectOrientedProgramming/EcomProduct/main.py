from  loggingmodule import logger
from exceptionmodule import InsufficientStockError, InvalidQuantityError
from product import Product

def main():
    logger.info("Starting E-commerce Application Demonstration.")

    #  Inventory Initialization (5 Different Products)
    inventory = []
    try:
        inventory.append(Product("P1001", "Wireless Mouse", 25.99, "Electronics", 50))
        inventory.append(Product("P1002", "Mechanical Keyboard", 89.99, "Electronics", 15))
        inventory.append(Product("P1003", "Ergonomic Office Chair", 249.50, "Furniture", 5))
        inventory.append(Product("P1004", "Stainless Steel Water Bottle", 19.95, "Home & Kitchen", 100))
        inventory.append(Product("P1005", "Running Shoes", 120.00, "Apparel", 30))
    except ValueError as e:
        logger.critical(f"Failed to initialize store inventory: {e}")
        return

    print("\n--- Current Inventory Status ---")
    for prod in inventory:
        prod.display_product()
    print("--------------------------------\n")

    #  Demonstration of Successful Purchases & Stock Updates
    logger.info("Scenario 1: Customer buys 2 Mechanical Keyboards.")
    keyboard = inventory[1]
    purchase_qty = 2
    
    try:
        total_cost = keyboard.calculate_total_price(purchase_qty)
        print(f"\n[Checkout] Total price for {purchase_qty}x {keyboard.name}: ${total_cost:.2f}")
        
        # Deduct stock for successful purchase
        keyboard.update_stock(-purchase_qty)
    except (InvalidQuantityError, InsufficientStockError) as e:
        logger.error(f"Purchase failed: {e}")

    #  Demonstration of Restocking Inventory
    logger.info("Scenario 2: Supplier restocks Office Chairs.")
    office_chair = inventory[2]
    office_chair.update_stock(10)  # Adding 10 more chairs to stock

    #  Demonstration of Exception Handling (Insufficient Stock)
    logger.info("Scenario 3: Customer attempts to buy 20 Running Shoes (Stock is 30).")
    shoes = inventory[4]
    
    try:
        # First purchase succeeds
        shoes.update_stock(-20)
        
        # Second purchase should trigger an error because only 10 remain
        logger.info("Scenario 4: Customer attempts to buy 15 more Running Shoes (Only 10 left).")
        shoes.update_stock(-15)
    except InsufficientStockError as e:
        logger.error(f"Expected Error Caught Successfully: {e}")

    #  Demonstration of Static Method Usage
    logger.info("Scenario 5: Testing price validation using the static method.")
    test_prices = [45.99, -5.00, 0]
    for price in test_prices:
        is_valid = Product.is_valid_price(price)
        logger.info(f"Is price ${price} valid? {is_valid}")

    print("\n--- Final Inventory Status ---")
    for prod in inventory:
        prod.display_product()
    print("------------------------------\n")
    
    logger.info("E-commerce Application Demonstration Completed.")

if __name__ == "__main__":
    main()