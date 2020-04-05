import pytest
import unittest
from service import UserService
from unittest.mock import Mock


# @pytest.fixture(scope="function")
# def user_service() -> None:
#     return Mock(spec=UserService)


# @pytest.mark.usefixtures("client")
class TestUserApi(unittest.TestCase):

    def setUp(self) -> None:
        self.service = Mock(spec=UserService)

    # @pytest.fixture(autouse=True)
    @pytest.mark.usefixtures("client")
    def test_list_user(self, client):
        self.service.list_user.return_value = [{'id': 1, 'name': 'admin', 'email': 'admin@example.com'}]
        rv = client.get('/api/v1/user/list')
        assert rv.status_code == 200
        assert len(rv.json['users']) == 0

