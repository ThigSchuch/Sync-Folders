import os

import pytest

from config import ConfigArgs

VALID_PATH = os.getcwd()
INVALID_PATH = "/invalid/path"


def test_initialization_with_valid_arguments():
    source_folder = VALID_PATH
    replica_folder = VALID_PATH
    interval_sync = 60
    log_file = "sync.log"

    config_args = ConfigArgs(source_folder, replica_folder, interval_sync, log_file)

    assert config_args.source_folder == source_folder
    assert config_args.replica_folder == replica_folder
    assert config_args.interval_sync == interval_sync
    assert config_args.log_file == log_file


def test_empty_source_folder_argument():
    source_folder = ""
    replica_folder = VALID_PATH
    interval_sync = 60
    log_file = "sync.log"

    with pytest.raises(Exception) as excinfo:
        ConfigArgs(source_folder, replica_folder, interval_sync, log_file)

    assert str(excinfo.value) == "Invalid configuration arguments, check your paths"


def test_default_values_for_interval_sync_and_log_file():
    config_args = ConfigArgs(VALID_PATH, VALID_PATH)

    assert config_args.source_folder == VALID_PATH
    assert config_args.replica_folder == VALID_PATH
    assert config_args.interval_sync == 60
    assert config_args.log_file == "sync.log"


def test_custom_values_interval_sync_log_file():
    source_folder = VALID_PATH
    replica_folder = VALID_PATH
    interval_sync = 30
    log_file = "custom.log"

    config_args = ConfigArgs(source_folder, replica_folder, interval_sync, log_file)

    assert config_args.source_folder == source_folder
    assert config_args.replica_folder == replica_folder
    assert config_args.interval_sync == interval_sync
    assert config_args.log_file == log_file


def test_valid_source_and_replica_folders():
    source_folder = VALID_PATH
    replica_folder = VALID_PATH
    interval_sync = 60
    log_file = "sync.log"

    config_args = ConfigArgs(source_folder, replica_folder, interval_sync, log_file)

    assert config_args.source_folder == source_folder
    assert config_args.replica_folder == replica_folder
    assert config_args.interval_sync == interval_sync
    assert config_args.log_file == log_file


def test_string_representation():
    source_folder = VALID_PATH
    replica_folder = VALID_PATH
    interval_sync = 60
    log_file = "sync.log"

    config_args = ConfigArgs(source_folder, replica_folder, interval_sync, log_file)

    assert str(config_args) == "ConfigArgs"


def test_empty_replica_folder_argument():
    source_folder = VALID_PATH
    replica_folder = ""
    interval_sync = 60
    log_file = "sync.log"

    with pytest.raises(Exception) as e:
        ConfigArgs(source_folder, replica_folder, interval_sync, log_file)


def test_negative_interval_sync_value():
    source_folder = VALID_PATH
    replica_folder = VALID_PATH
    interval_sync = -10
    log_file = "sync.log"

    with pytest.raises(Exception) as e:
        ConfigArgs(source_folder, replica_folder, interval_sync, log_file)


def test_non_integer_interval_sync_value():
    with pytest.raises(Exception) as e:
        ConfigArgs(VALID_PATH, VALID_PATH, "invalid", "sync.log")
    assert str(e.value) == "Invalid configuration arguments, check your paths"


def test_invalid_source_folder_path():
    invalid_source_folder = ""
    replica_folder = VALID_PATH
    interval_sync = 60
    log_file = "sync.log"

    with pytest.raises(Exception) as e:
        ConfigArgs(invalid_source_folder, replica_folder, interval_sync, log_file)


def test_invalid_replica_folder_path():
    invalid_source_folder = VALID_PATH
    invalid_replica_folder = ""
    interval_sync = 60
    log_file = "sync.log"

    with pytest.raises(Exception) as e:
        ConfigArgs(
            invalid_source_folder, invalid_replica_folder, interval_sync, log_file
        )
