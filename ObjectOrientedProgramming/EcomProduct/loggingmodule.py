import logging

def set_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='product.log',
                        filemode='a')
    return logging.getLogger('product_logger')

logger = set_logger()