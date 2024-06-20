import os

from utils import files_are_equal


def test_one_or_both_files_do_not_exist():
    file1 = "non_existent_file1.txt"
    file2 = "non_existent_file2.txt"

    assert files_are_equal(file1, file2) == False

    with open(file1, "wb") as f:
        f.write(b"Hello, World!")

    assert files_are_equal(file1, file2) == False

    os.remove(file1)


def test_files_with_different_content_return_false():
    file1 = "test_file1.txt"
    file2 = "test_file2.txt"
    content1 = b"Hello, World!"
    content2 = b"Goodbye, World!"

    with open(file1, "wb") as f:
        f.write(content1)
    with open(file2, "wb") as f:
        f.write(content2)

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)


def test_large_files_with_identical_content_return_false():
    file1 = "large_file1.txt"
    file2 = "large_file2.txt"
    content = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    with open(file1, "wb") as f:
        f.write(content)
    with open(file2, "wb") as f:
        f.write(content)

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)


def test_files_with_same_size_different_content_return_false():
    file1 = "test_file1.txt"
    file2 = "test_file2.txt"
    content1 = b"Hello, World!"
    content2 = b"Goodbye, World!"

    with open(file1, "wb") as f:
        f.write(content1)
    with open(file2, "wb") as f:
        f.write(content2)

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)


def test_files_with_different_content_return_false():
    file1 = "large_file1.txt"
    file2 = "large_file2.txt"
    content1 = b"Large file content 1"
    content2 = b"Large file content 2"

    with open(file1, "wb") as f:
        f.write(content1)
    with open(file2, "wb") as f:
        f.write(content2)

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)


def test_one_file_empty_and_other_not():
    file1 = "empty_file.txt"
    file2 = "non_empty_file.txt"

    # Create an empty file
    open(file1, "w").close()

    # Write content to the non-empty file
    with open(file2, "wb") as f:
        f.write(b"Hello, World!")

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)


def test_files_with_different_sizes_return_false():
    file1 = "test_file1.txt"
    file2 = "test_file2.txt"
    content1 = b"Hello, World!"
    content2 = b"Hello, World!123"

    with open(file1, "wb") as f:
        f.write(content1)
    with open(file2, "wb") as f:
        f.write(content2)

    assert files_are_equal(file1, file2) == False

    os.remove(file1)
    os.remove(file2)
