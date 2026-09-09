import logging
import os

def setup_logging():
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Base logger configuration
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)  # Capture everything at the root level

    # Prevent duplicate logs if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Define a clean, professional log format
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 1. Application Log Handler (Tracks everything)
    app_handler = logging.FileHandler('logs/application.log')
    app_handler.setLevel(logging.DEBUG)
    app_handler.setFormatter(log_format)

    # 2. Error Log Handler (Tracks WARNING, ERROR, CRITICAL)
    error_handler = logging.FileHandler('logs/error.log')
    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(app_handler)
    logger.addHandler(error_handler)

    return logger

# Initialize the logger instance for other modules to import
log = setup_logging()