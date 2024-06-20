import json
import os

from config import ConfigFile

VALID_PATH = os.getcwd()
INVALID_PATH = "/invalid/path"
VALID_LOG = f"{VALID_PATH}/sync.log"


def test_initialization_with_valid_config_file(mocker):
    mock_open = mocker.mock_open(
        read_data=json.dumps(
            {
                "source_folder": VALID_PATH,
                "replica_folder": VALID_PATH,
                "interval_sync": 30,
                "log_file": VALID_LOG,
            }
        )
    )
    mocker.patch("builtins.open", mock_open)

    config = ConfigFile()

    assert config.source_folder == VALID_PATH
    assert config.replica_folder == VALID_PATH
    assert config.interval_sync == 30
    assert config.log_file == VALID_LOG


def test_get_interval_validates_and_returns_interval(mocker):
    mocker.patch("builtins.input", return_value="10")

    interval = ConfigFile.get_interval()

    assert interval == 10


def test_valid_configs_method(mocker):
    mocker.patch(
        "builtins.input",
        side_effect=[VALID_PATH, VALID_PATH, "30", VALID_LOG],
    )

    config = ConfigFile()

    assert config.valid_configs() == True


def test_get_interval_non_integer_input(mocker):
    mocker.patch("builtins.input", side_effect=["abc", "def", "50"])

    interval = ConfigFile.get_interval()

    assert interval == 50


def test_get_configs_loads_configurations(mocker):
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("os.path.getsize", return_value=100)

    mock_open = mocker.mock_open(
        read_data=json.dumps(
            {
                "source_folder": VALID_PATH,
                "replica_folder": VALID_PATH,
                "interval_sync": 30,
                "log_file": VALID_LOG,
            }
        )
    )
    mocker.patch("builtins.open", mock_open)

    config = ConfigFile()

    assert config.source_folder == VALID_PATH
    assert config.replica_folder == VALID_PATH
    assert config.interval_sync == 30
    assert config.log_file == VALID_LOG
