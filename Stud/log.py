import logging
import sys

# Configure logging for both file and console output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('stud.log', mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

def log_msg(level, msg):
    logger = logging.getLogger(__name__)
    log_funcs = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "debug": logger.debug
    }
    
    # Check if the level is valid and call the function
    if level.lower() in log_funcs:
        log_funcs[level.lower()](msg)
    else:
        logger.error(f"Invalid log level: {level}")

# Example usage:
#log_msg("info", "This is an info message")
#log_msg("error", "This is an error message")