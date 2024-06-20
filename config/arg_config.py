from .absconfig import AbstractConfig


class ConfigArgs(AbstractConfig):
    """
    ConfigArgs class represents a configuration object with specific arguments for source folder,
    replica folder, interval sync, and log file.
    It inherits from AbstractConfig class and validates the configuration arguments upon initialization.
    If the configuration arguments are invalid, an exception is raised.

    Attributes:
        source_folder (str): The source folder path.
        replica_folder (str): The replica folder path.
        interval_sync (int): The interval for synchronization (default is 60 seconds).
        log_file (str): The log file path (default is "sync.log").

    Methods:
        __init__: Initializes the ConfigArgs object with the provided configuration arguments and validates them.
        __str__: Returns a string representation of the ConfigArgs object.

    Inherits from:
        AbstractConfig: An abstract base class defining common configuration attributes and a method for validating configurations.
    """

    def __init__(
        self,
        source_folder: str,
        replica_folder: str,
        interval_sync: int = 60,
        log_file: str = "sync.log",
    ):
        print("Using configuration arguments")

        self.source_folder: str = source_folder
        self.replica_folder: str = replica_folder
        self.interval_sync: int = interval_sync
        self.log_file: str = log_file

        if not self.valid_configs():
            raise Exception("Invalid configuration arguments, check your paths")

    def __str__(self):
        return "ConfigArgs"
