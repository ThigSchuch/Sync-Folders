from abc import ABC

from utils import valid_path_folder


class AbstractConfig(ABC):
    """
    This class represents an abstract configuration for syncing folders.

    Attributes:
        source_folder (str): The source folder path for syncing.
        replica_folder (str): The replica folder path for syncing.
        interval_sync (int): The interval in seconds for syncing.
        log_file (str): The path to the log file.

    Methods:
        valid_configs(): Checks if the configuration arguments are valid by verifying the source and replica folders.
    """

    def __init__(self):
        self.source_folder: str = ...
        self.replica_folder: str = ...
        self.interval_sync: int = ...
        self.log_file: str = ...

    def valid_configs(self) -> bool:
        """
        Check if the configuration arguments are valid by verifying the source and replica folders.

        Returns:
            bool: True if the configuration arguments are valid, False otherwise.
        """
        if not self.source_folder or not self.replica_folder:
            return False

        if not valid_path_folder(self.source_folder) or not valid_path_folder(
            self.replica_folder
        ):
            return False

        if (
            self.interval_sync
            and not isinstance(self.interval_sync, int)
            or self.interval_sync <= 0
        ):
            return False

        return True

    def __str__(self):
        return "Config"
