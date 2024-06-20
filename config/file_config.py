import json
import os

from config.absconfig import AbstractConfig
from utils import create_folder, valid_path_folder


class ConfigFile(AbstractConfig):
    """
    This class represents a configuration file for syncing folders, inheriting from the AbstractConfig class.

    Attributes:
        config_file (str): The path to the configuration file.
        source_folder (str): The source folder path for syncing.
        replica_folder (str): The replica folder path for syncing.
        interval_sync (int): The interval in seconds for syncing.
        log_file (str): The path to the log file.

    Methods:
        valid_configs(): Checks if the configuration file is valid by verifying the source and replica folders.
        get_folder(folder_name: str) -> str: Get the folder path.
        get_interval() -> int: Get the interval sync in seconds.
        get_log_file() -> str: Get the log file path.
        initial_setup() -> None: Initial setup method for inputting values and writing to the configuration file.
        get_configs() -> json: Get the configuration file loaded as a JSON object.
        reset_configs() -> None: Reset the configuration file by overwriting its content.
        write_configs(key: str, value: str) -> bool: Write the configuration file with a key-value pair.

    Raises:
        Exception: If the configuration file is invalid.

    Inherits:
        AbstractConfig: An abstract class representing a configuration for syncing folders.
    """

    def __init__(self):
        print("Using configuration file")
        self.config_file: str = "config.json"
        self.source_folder: str = ""
        self.replica_folder: str = ""
        self.interval_sync: int = 60
        self.log_file: str = "sync.log"

        self.get_configs()

        if not self.source_folder or not self.replica_folder:
            self.initial_setup()

        if not self.valid_configs():
            if (
                input("Do you want to reset the configuration file? (y/n): ").lower()
                == "y"
            ):
                self.reset_configs()
                self.initial_setup()
            else:
                raise Exception("Invalid configuration file")

    def __str__(self):
        return "ConfigFile"

    def valid_configs(self) -> bool:
        """
        Check if the configuration file is valid

        Returns:
            bool: True if the source_folder or replica_folder is empty, False otherwise
        """
        if not self.source_folder or not self.replica_folder:
            return True
        return super().valid_configs()

    @staticmethod
    def get_folder(folder_name: str) -> str:
        """
        Get the folder path.

        This method prompts the user to input the folder path with the provided folder_name.
        It then checks if the input path is a valid folder using the 'valid_path_folder' function.
        If the path is not valid, it creates the folder using the 'create_folder' function.
        The method continues to prompt the user until a valid folder path is provided.
        The final validated folder path is returned as a string.

        Parameters:
            folder_name (str): The name of the folder for which the path is being entered.

        Returns:
            str: The validated folder path.
        """
        folder: str = input(f"Enter the {folder_name} folder: ")
        while not valid_path_folder(folder):
            created, folder = create_folder(folder)
            if created:
                break
            folder = input(f"Enter the {folder_name} folder: ")
        return folder

    @staticmethod
    def get_interval() -> int:
        """
        Get the interval sync in seconds.

        This method prompts the user to input the interval sync in seconds, defaulting to 60 if no input is provided.
        It then validates the input by converting it to an integer. If the input is not a valid integer, it continues to prompt the user until a valid input is provided.
        The final interval sync value is returned as an integer.

        Returns:
            int: The validated interval sync value in seconds.
        """
        DEFAULT = 60
        interval: int = (
            input(f"Enter the interval sync in seconds ({DEFAULT}): ") or DEFAULT
        )
        exception = True
        while exception:
            try:
                interval = int(interval)
                exception = False
            except Exception as e:
                interval = (
                    input(f"Enter the interval sync in seconds ({DEFAULT}): ")
                    or DEFAULT
                )
        return interval

    @staticmethod
    def get_log_file() -> str:
        """
        Get the log file path.

        This method prompts the user to input the log file path, defaulting to 'sync.log' if no input is provided.
        It then validates the input by checking if the path is a valid folder using the 'valid_path_folder' function.
        If the path is not a valid folder, it creates the folder using the 'create_folder' function.
        The final log file path is returned as a string.

        Returns:
            str: The validated log file path.
        """
        DEFAULT = "sync.log"
        log_file: str = input(f"Enter the log file ({DEFAULT}): ") or DEFAULT
        log_path = "/".join(log_file.split("/")[:-1])

        if log_path:
            while not valid_path_folder(log_path):
                created, log_path = create_folder(log_path)
                if created:
                    break

                log_file = input(f"Enter the log file ({DEFAULT}): ") or DEFAULT
                log_path = "/".join(log_file.split("/")[:-1])
        else:
            log_path = os.getcwd()
        return f"{log_path}/{log_file}"

    def initial_setup(self) -> None:
        """
        Initial setup method that prompts the user to input values for source_folder, replica_folder, interval_sync, and log_file.
        It then writes these values to the configuration file using the write_configs method and updates the corresponding attributes in the class instance.

        Parameters:
            None

        Returns:
            None
        """
        print("Initial setup")

        attributes = {
            "source_folder": self.get_folder("source"),
            "replica_folder": self.get_folder("replica"),
            "interval_sync": self.get_interval(),
            "log_file": self.get_log_file(),
        }

        for key, value in attributes.items():
            self.write_configs(key, value)
            self.__dict__[key] = value

    def get_configs(self) -> json:
        """
        Get the configuration file

        Returns:
            json: The configuration file loaded as a JSON object.
        """
        if (
            not os.path.exists(self.config_file)
            or os.path.getsize(self.config_file) == 0
        ):
            with open(self.config_file, "w") as f:
                f.write("{}")

        with open(self.config_file, "r") as f:
            config_file: json = json.load(f)

            for key, value in config_file.items():
                self.__dict__[key] = value

            return config_file

    def reset_configs(self) -> None:
        """
        Reset the configuration file

        This method opens the configuration file in write mode and overwrites its content with an empty JSON object '{}'.

        Returns:
            None
        """
        with open(self.config_file, "w") as f:
            f.write("{}")

    def write_configs(self, key: str, value: str) -> bool:
        """
        Write the configuration file

        Parameters:
            key (str): The key to be written in the configuration file.
            value (str): The value corresponding to the key to be written in the configuration file.

        Returns:
            bool: True if the writing is successful, False otherwise.
        """
        config_file: json = self.get_configs()
        config_file[key] = value

        try:
            with open(self.config_file, "w") as f:
                json.dump(config_file, f)
            return True

        except Exception as e:
            print(e)
            return False
