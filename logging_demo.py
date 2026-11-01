import logging


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")


a = 10
b = 0

logging.info("Performing division operation")

try:
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    logging.exception("Division by zero is not allowed")

print("Program executed successfully!")