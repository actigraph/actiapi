import os

import pytest

from actiapi.v3 import ActiGraphClientV3


@pytest.fixture(scope="session")
def v3_access_key():
    return os.environ.get("API_ACCESS_KEY", "")


@pytest.fixture(scope="session")
def v3_secret_key():
    return os.environ.get("API_SECRET_KEY", "")


@pytest.fixture(scope="session")
def v3_study_id():
    return 954


@pytest.fixture(scope="session")
def v3_client(v3_access_key, v3_secret_key):
    client = ActiGraphClientV3(v3_access_key, v3_secret_key)
    return client
