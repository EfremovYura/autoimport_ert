from client.utils import load_data
from client.config import DATA_FILE_NAME


def test_load_data():
    result = load_data(DATA_FILE_NAME)

    assert isinstance(result, dict)
