import rich
from rich import print as log
from rich.console import Console
import datetime
import os


class Logger:
    def __init__(self, log_file_name="log.txt", log_dir="logs"):
        self.console = Console()
        self.log_file_name = log_file_name  # Name of the log file
        self.log_directory = log_dir  # Directory where the log file will be stored
        # Create the log directory if it doesn't exist
        os.makedirs(self.log_directory, exist_ok=True)
        self.log_file = self.LogFile(self)  # Create the log file

    class LogFile:
        def __init__(self, parent):
            self.parent = parent

        def log(self, message, log_type):
            # Create the full log file path
            log_file_path = os.path.join(
                self.parent.log_directory, self.parent.log_file_name)  # Path to the log file
            # Current time in the format "YYYY-MM-DD|HH:MM:SS"
            current_time = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")

            # Write the log entry
            with open(log_file_path, "a+") as log_file:
                # Write the log entry
                log_file.write(f"{current_time} [{log_type}] {message}\n")

    class LogPrint:
        def __init__(self, parent):
            self.parent = parent

        def error(self, message):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
            log(f"[blue]{current_time}[/blue] [red][bold][ERROR][/bold] {message}[/red]")
            # Write the log entry to the console
            self.parent.log_file.log(message, "ERROR")

        def info(self, message):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
            log(f"[blue]{current_time}[/blue] [green][bold][INFO][/bold] {message}[/green]")
            # Write the log entry to the console
            self.parent.log_file.log(message, "INFO")

        def warn(self, message):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
            log(f"[blue]{current_time}[/blue] [yellow][bold][WARN][/bold] {message}[/yellow]")
            # Write the log entry to the console
            self.parent.log_file.log(message, "WARN")

        def debug(self, message):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
            log(f"[blue]{current_time}[/blue] [cyan][bold][DEBUG][/bold] {message}[/cyan]")
            # Write the log entry to the console
            self.parent.log_file.log(message, "DEBUG")


# Usage
logger = Logger()
log_printer = logger.LogPrint(logger)
log_printer.error("This is a test error message")
log_printer.warn("This is a test warn message")
log_printer.info("This is a test info message")
log_printer.debug("This is a test debug message")
