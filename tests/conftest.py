import pytest

from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()
