import sys
from logger_config import log
import calculator
import file_operations

# Dummy user database
USERNAMES = ["admin", "user1"]

def main():
    log.info("Application started.")
    is_logged_in = False
    
    while True:
        try:
            print("\n=========================")
            print("        MAIN MENU        ")
            print("=========================")
            print("1. Login")
            print("2. Calculate")
            print("3. Read a File")
            print("4. Write a File")
            print("5. Logout")
            print("6. Exit Application")
            print("=========================")
            
            choice = input("Select an option (1-6): ").strip()
            
            # --- 1. LOGIN ---
            if choice == "1":
                if is_logged_in:
                    print("You are already logged in!")
                    continue
                
                username = input("Enter username: ").strip()
                if username in USERNAMES:
                    is_logged_in = True
                    print(f"Welcome, {username}!")
                    log.info(f"User '{username}' logged in.")
                else:
                    print("Invalid username!")
                    log.warning(f"Failed login attempt with username: '{username}'")

            # --- PROTECTED ROUTES (Must be logged in) ---
            elif choice in ["2", "3", "4", "5"]:
                if not is_logged_in:
                    print("Access Denied. You must log in first!")
                    log.warning(f"Unauthorized access attempt to menu option {choice}.")
                    continue
                
                if choice == "2":
                    calculator.perform_calculation()
                elif choice == "3":
                    file_operations.read_file()
                elif choice == "4":
                    file_operations.write_file()
                elif choice == "5":
                    is_logged_in = False
                    print("You have logged out successfully.")
                    log.info("User logged out.")
            
            # --- 6. EXIT ---
            elif choice == "6":
                print("Goodbye!")
                log.info("Application closed normally by user.")
                sys.exit(0)
                
            else:
                print("Invalid choice! Please choose a number between 1 and 6.")
                log.debug(f"User entered an invalid menu choice: '{choice}'")
                
        except KeyboardInterrupt:
            # Catching Ctrl+C gently
            print("\nApplication interrupted. Exiting...")
            log.warning("Application interrupted via KeyboardInterrupt (Ctrl+C).")
            sys.exit(0)
            
        except Exception as e:
            # CRITICAL fallback exception handler to keep the app alive
            print("\nA critical application error occurred! The program will reset to the menu.")
            log.critical(f"Unexpected application failure: {e}", exc_info=True)

if __name__ == "__main__":
    main()