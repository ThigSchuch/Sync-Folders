import os

VALID_PATH = os.getcwd()
INVALID_PATH = "/invalid/path"


def test_valid_configs_returns_true_for_valid_folders():
    from config.absconfig import AbstractConfig

    config = AbstractConfig()
    config.source_folder = VALID_PATH
    config.replica_folder = VALID_PATH
    config.interval_sync = 60

    assert config.valid_configs() is True


def test_valid_configs_returns_false_when_replica_folder_is_empty():
    from config.absconfig import AbstractConfig

    config = AbstractConfig()
    config.source_folder = VALID_PATH
    config.replica_folder = ""
    config.interval_sync = 60

    assert config.valid_configs() is False


def test_valid_configs_returns_false_when_source_folder_is_empty():
    from config.absconfig import AbstractConfig

    config = AbstractConfig()
    config.source_folder = ""
    config.replica_folder = VALID_PATH
    config.interval_sync = 60

    assert config.valid_configs() is False


def test_valid_configs_returns_false_for_invalid_source_folder():
    from config.absconfig import AbstractConfig

    config = AbstractConfig()
    config.source_folder = INVALID_PATH
    config.replica_folder = VALID_PATH
    config.interval_sync = 60

    assert config.valid_configs() is False


def test_valid_configs_returns_false_for_invalid_replica_folder():
    from config.absconfig import AbstractConfig

    config = AbstractConfig()
    config.source_folder = VALID_PATH
    config.replica_folder = INVALID_PATH
    config.interval_sync = 60

    assert config.valid_configs() is False
