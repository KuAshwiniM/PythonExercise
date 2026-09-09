import os
from logger_config import log

FILE_NAME = "sample.txt"

def read_file():
    log.debug("Entering read file module.")
    print("\n--- Read File ---")
    
    try:
        if not os.path.exists(FILE_NAME):
            raise FileNotFoundError(f"The file '{FILE_NAME}' does not exist yet.")
            
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            
            if not content.strip():
                print("The file is empty.")
                log.warning(f"File '{FILE_NAME}' was read, but it was empty.")
            else:
                print("File Content:")
                print(content)
                log.info(f"File '{FILE_NAME}' read successfully.")
                
    except FileNotFoundError as e:
        print(f"Error: {e}")
        log.error(f"File could not be opened: {e}")
    except Exception as e:
        print(f"An unexpected file error occurred: {e}")
        log.critical(f"Unexpected application failure during file read: {e}")

def write_file():
    log.debug("Entering write file module.")
    print("\n--- Write File ---")
    
    try:
        text = input("Enter the text you want to save to the file: ")
        
        with open(FILE_NAME, 'w') as file:
            file.write(text)
            
        print(f"Successfully saved to {FILE_NAME}!")
        log.info(f"File '{FILE_NAME}' updated successfully.")
        
    except Exception as e:
        print(f"Error: Could not write to file. {e}")
        log.error(f"File could not be written to. Details: {e}")