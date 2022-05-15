import logging

logging.basicConfig(filename = "E:\\python_code\\new_sdet_pract\\selemniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%y  %I:%M:%S %p",
                    level=logging.DEBUG
                    )

logging.debug("THIS IS A DEBUG MESSAGE")
logging.info("THIS IS A INFO MESSAGE")
logging.warning("THIS IS A WARNING MESSAGE")
logging.error("THIS IS A ERROR MESSAGE")
logging.critical("THIS IS A CRITICAL MESSAGE")

