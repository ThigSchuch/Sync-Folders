import os

from utils import valid_path_folder


def test_valid_absolute_path_to_existing_directory():
    path = os.path.abspath(os.path.dirname(__file__))
    assert valid_path_folder(path) == True


def test_empty_string_path():
    path = ""
    assert valid_path_folder(path) == False


def test_valid_absolute_path_to_non_existing_directory():
    path = "/path/to/non_existing_directory"
    assert valid_path_folder(path) == False


def test_valid_absolute_path_to_file_returns_false():
    path = os.path.abspath(__file__)
    assert valid_path_folder(path) == False


def test_relative_path_to_existing_directory_returns_false():
    path = "relative/path/to/existing/directory"
    assert valid_path_folder(path) == False


def test_path_with_special_characters_invalid_directory_returns_false():
    path = "C:/Users/!@#$%^&*()_+/Desktop/invalid_folder"
    assert valid_path_folder(path) == False


def test_path_with_trailing_slash_returns_true_if_directory_exists():
    path = os.path.abspath(os.path.dirname(__file__)) + "/"
    assert valid_path_folder(path) == True
