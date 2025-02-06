# Usage

```Python
# Initialize the logger with the settings you want:
logger = Logger(log_file_name, log_dir, log_level) # defaults are log.txt, logs and DEBUG
log_printer = logger.LogPrint(logger)
# Logging(will also log to a file):
log_printer.error("This is a test error message")
log_printer.warn("This is a test warn message")
log_printer.info("This is a test info message")
log_printer.debug("This is a test debug message")
try:
    1/0
except Exception as e:
    log_printer.error("This is a test error message with an Exception", e)
```
