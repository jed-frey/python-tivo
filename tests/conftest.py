import uuid

import pytest


@pytest.fixture(scope="session")
def session_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="module")
def module_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="class")
def class_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="function")
def function_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="session")
def tivo():
    import tivo
    yield tivo.TiVo(host="192.168.1.135", port=31339)
