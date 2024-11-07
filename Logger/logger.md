# Usage

```Python
# Initialize the logger:
logger = Logger()
log_printer = logger.LogPrint(logger)
# Logging(will also log to a file):
log_printer.error("This is a test error message")
log_printer.warn("This is a test warn message")
log_printer.info("This is a test info message")
log_printer.debug("This is a test debug message")
```
