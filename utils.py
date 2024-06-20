import hashlib
import os


def files_are_equal(file1: str, file2: str) -> bool:
    """
    Check if two files are equal by comparing their content using MD5 hash.
    :param file1: str - The path to the first file to be compared.
    :param file2: str - The path to the second file to be compared.
    :return: bool - True if the files have the same content, False otherwise.
    """

    if not os.path.exists(file1) or not os.path.exists(file2):
        return False

    if os.path.getsize(file1) != os.path.getsize(file2):
        return False

    if file1.split("/")[-1] != file2.split("/")[-1]:
        return False

    hash1 = hashlib.md5()
    hash2 = hashlib.md5()

    with open(file1, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash1.update(chunk)

    with open(file2, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash2.update(chunk)

    return hash1.hexdigest() == hash2.hexdigest()


def valid_path_folder(path: str) -> bool:
    """
    Check if the provided path is a valid absolute path to an existing directory.
    :param path: str - The path to be validated.
    :return: bool - True if the path is a valid absolute path to an existing directory, False otherwise.
    """
    if not os.path.isabs(path):
        return False

    if os.path.exists(path) and os.path.isdir(path):
        return True

    return False


def create_folder(path: str) -> tuple[bool, str]:
    """
    Create a folder at the specified path if it does not already exist.
    If the provided path is not a full path, it will be created relative to the current working directory after user confirmation.
    :param path: str - The path where the folder should be created.
    :return: tuple[bool, str] - A tuple containing a boolean indicating if the folder was successfully created
    and the final path where the folder is located.
    """
    if not os.path.isabs(path):
        new_path = os.path.join(os.getcwd(), path)

        if (
            input(
                f"{path} is not a full path, create folder at {new_path}? (y/n): "
            ).lower()
            == "y"
        ):
            os.makedirs(new_path, exist_ok=True)
            return True, new_path

        return False, path

    else:
        os.makedirs(path, exist_ok=True)
        return True, path
