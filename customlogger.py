import logging ## for log the activity

# logging.info("hello this is my first logging file")

# logging.basicConfig(
#     filename="app.log",
#     format='[%(asctime)s : %(level)s-%(name)s - %(message)s]',
#     level= logging.DEBUG  #levels in assecding DEBUG<INFO<WARN<ERROR<CRITICAL
# )

logger = logging.getLogger("interview_logger")
logger.setLevel(logging.DEBUG)

formater = logging.Formatter('[%(asctime)s : %(levelname)s - %(name)s - %(message)s]')


fileLogger = logging.FileHandler("app.log")
fileLogger.setLevel(logging.WARN)
fileLogger.setFormatter(formater)


console_logger = logging.StreamHandler()
console_logger.setLevel(logging.INFO)
console_logger.setFormatter(formater)


logger.addHandler(fileLogger)
logger.addHandler(console_logger)

