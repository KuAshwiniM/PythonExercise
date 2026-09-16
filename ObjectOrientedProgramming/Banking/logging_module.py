import logging

def setup_logger():
    logging.basicConfig(
        filename="bank_operations.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("BankLogger")

logger = setup_logger()