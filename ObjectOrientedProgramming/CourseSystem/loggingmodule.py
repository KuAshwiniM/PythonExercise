import logging

def setup_logging():
    """
    Sets up the logging configuration for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("course.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('course_logger')\

logger = setup_logging()