import logging

logging.basicConfig(filename = "E:\\python_code\\new_sdet_pract\\selemniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%y  %I:%M:%S %p"
                    )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("THIS IS A DEBUG MESSAGE")
logger.info("THIS IS A INFO MESSAGE")
logger.warning("THIS IS A WARNING MESSAGE")
logger.error("THIS IS A ERROR MESSAGE")
logger.critical("THIS IS A CRITICAL MESSAGE")

