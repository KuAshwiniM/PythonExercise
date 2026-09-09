from logger_config import log

def perform_calculation():
    log.debug("Entering calculation module.")
    print("\n--- Simple Calculator (Division) ---")
    
    try:
        num1 = float(input("Enter numerator (number to divide): "))
        num2 = float(input("Enter denominator (number to divide by): "))
        
        # This will trigger an error if num2 is 0
        result = num1 / num2
        
        print(f"Result: {result}")
        log.info(f"Calculation completed successfully: {num1} / {num2} = {result}")
        
    except ZeroDivisionError as e:
        print("Error: You cannot divide by zero!")
        log.error(f"Calculation failed: Division by zero attempted. Details: {e}")
    except ValueError as e:
        print("Error: Please enter valid numbers.")
        log.error(f"Calculation failed: Invalid numerical input. Details: {e}")