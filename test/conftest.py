import pytest
from starter import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app('test')
    return app


@pytest.fixture(scope="session")
def logger(app):
    logger = app.logger
    return logger


class TestResource(object):
    def test_that_depends_on_resource(self, resource):
        print("testing {}".format(resource))
