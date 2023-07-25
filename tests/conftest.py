import os

import pytest

from actiapi.v2 import ActiGraphClientV2
from actiapi.v3 import ActiGraphClientV3


@pytest.fixture(scope="session")
def v2_access_key():
    return os.environ.get("API_ACCESS_KEY_V2", "")


@pytest.fixture(scope="session")
def v2_secret_key():
    return os.environ.get("API_SECRET_KEY_V2", "")


@pytest.fixture(scope="session")
def v2_study_id():
    return 954


@pytest.fixture(scope="session")
def v2_client(v2_access_key, v2_secret_key):
    client = ActiGraphClientV2(v2_access_key, v2_secret_key)
    return client


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
def v3_user():
    return 55212


@pytest.fixture(scope="session")
def v3_client(v3_access_key, v3_secret_key):
    client = ActiGraphClientV3(v3_access_key, v3_secret_key)
    return client


@pytest.fixture(scope="session")
def response_404():
    """Simulate an Http response with status code 404."""

    class Response:
        status_code = 404

    return Response()
