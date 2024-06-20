import os
import shutil
import time
from datetime import datetime
from pathlib import Path

from config import ConfigArgs, ConfigFile
from utils import files_are_equal

LOG_FILE: str = "sync.log"


class Sync:
    """
    Sync class represents a synchronization utility that manages the syncing
    of folders between a specified source and replica based
    on the provided configuration.
    It includes methods for creating, deleting, copying, and updating files and folders.
    The synchronization process can be initiated using the 'start' method,
    which continuously syncs the folders based on the configured interval.

    Attributes:
        config (ConfigArgs | ConfigFile): The configuration object containing the source folder,
        replica folder, interval sync, and log file settings.

    Methods:
        logger(func): Decorator function for logging method calls.
        sync_folders(source_folder: Path, replica_folder: Path) -> bool: Sync the folders between the specified source and replica paths.
        create_folder(folder: str) -> bool: Create a folder at the specified path.
        delete_folder(folder: str) -> bool: Delete a folder at the specified path.
        delete_file(file: str) -> bool: Delete a file at the specified path.
        copy_file(source_file: str, replica_file: str) -> bool: Copy a file from the source path to the replica path.
        update_file(source_file: str, replica_file: str) -> bool: Update a file by replacing it with a new version from the source path.
        start(): Start the synchronization process by continuously syncing the folders based on the configured interval.
    """

    def __init__(
        self,
        configuration: ConfigArgs | ConfigFile,
    ):
        self.config = configuration

        global LOG_FILE
        LOG_FILE = self.config.log_file

    def __str__(self):
        return "Sync"

    def logger(func):
        """
        Decorator function for logging method calls.

        Args:
            func: The function to be decorated.

        Returns:
            The result of the decorated function.

        Example:
            @logger
            def some_function(arg1, arg2):
                # do something
                return result
        """

        def wrapper(*args, **kwargs):
            operation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print_args = args

            if args and hasattr(args[0], "__class__"):
                print_args = args[1:]

            message = f"{operation_time}|{func.__name__}|{print_args}|{kwargs}"
            print(message)

            with open(LOG_FILE, "a") as f:
                f.write(f"{message}\n")

            result = func(*args, **kwargs)
            return result

        return wrapper

    def sync_folders(self, source_folder: Path, replica_folder: Path) -> bool:
        """
        Sync the folders

        Parameters:
            source_folder (Path): The source folder to sync from.
            replica_folder (Path): The replica folder to sync to.

        Returns:
            bool: True if the synchronization is successful, False otherwise.
        """
        if not os.path.exists(replica_folder):
            self.create_folder(replica_folder)

        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_file = os.path.join(root, file)
                replica_file = source_file.replace(source_folder, replica_folder)

                if not os.path.exists(replica_file):
                    self.copy_file(source_file, replica_file)
                    continue

                if not files_are_equal(source_file, replica_file):
                    self.update_file(source_file, replica_file)
                    continue

            for dest_root, dest_dirs, dest_files in os.walk(replica_folder):
                for file in dest_files:
                    replica_file = os.path.join(dest_root, file)
                    source_file = replica_file.replace(replica_folder, source_folder)

                    if not os.path.exists(source_file):
                        self.delete_file(replica_file)

                for dest_dir in dest_dirs:
                    replica_dir = os.path.join(dest_root, dest_dir)
                    source_dir = replica_dir.replace(replica_folder, source_folder)

                    if not os.path.exists(source_dir):
                        self.delete_folder(replica_dir)

            for dir in dirs:
                self.sync_folders(
                    os.path.join(source_folder, dir),
                    os.path.join(replica_folder, dir),
                )

        return True

    @logger
    def create_folder(self, folder: str) -> bool:
        """
        Create a folder

        Parameters:
            folder (str): The path of the folder to be created.

        Returns:
            bool: True if the folder is successfully created, False otherwise.
        """
        try:
            os.makedirs(folder)
            return True
        except Exception as e:
            print(e)
            return False

    @logger
    def delete_folder(self, folder: str) -> bool:
        """
        Delete a folder

        Parameters:
            folder (str): The path of the folder to be deleted.

        Returns:
            bool: True if the folder is successfully deleted, False otherwise.
        """
        try:
            shutil.rmtree(folder)
            return True
        except Exception as e:
            print(e)
            return False

    @logger
    def delete_file(self, file: str) -> bool:
        """
        Delete a file

        Parameters:
            file (str): The path of the file to be deleted.

        Returns:
            bool: True if the file is successfully deleted, False otherwise.
        """
        try:
            os.remove(file)
            return True
        except Exception as e:
            print(e)
            return False

    @logger
    def copy_file(self, source_file: str, replica_file: str) -> bool:
        """
        Copy files from source to replica

        Parameters:
            source_file (str): The path of the source file to be copied.
            replica_file (str): The path where the file will be copied to.

        Returns:
            bool: True if the file is successfully copied, False otherwise.
        """
        try:
            shutil.copy2(source_file, replica_file)
            return True
        except Exception as e:
            print(e)
            return False

    @logger
    def update_file(self, source_file: str, replica_file: str) -> bool:
        """
        Update files from source to replica

        Parameters:
            source_file (str): The path of the source file to be updated.
            replica_file (str): The path where the file will be updated to.

        Returns:
            bool: True if the file is successfully updated, False otherwise.
        """
        try:
            os.remove(replica_file)
            shutil.copy2(source_file, replica_file)
            return True
        except Exception as e:
            print(e)
            return False

    def start(self):
        """
        Start the synchronization process.

        This method continuously syncs the folders between the specified source and replica folders based on the configured interval. It calls the 'sync_folders' method to perform the synchronization operation.

        Parameters:
            None

        Returns:
            None
        """
        while True:
            print("Syncing folders...")
            self.sync_folders(self.config.source_folder, self.config.replica_folder)
            time.sleep(self.config.interval_sync)
