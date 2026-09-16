import logging

def setup_logger():
    logging.basicConfig(
        filename="employee_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("EmployeeApp")

logger = setup_logger()