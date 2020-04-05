import unittest
from unittest.mock import Mock
from model import User
from service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self) -> None:
        print('setup')
        self.service = Mock(spec=UserService)

    def test_exist(self):
        test_user_name = 'admin'
        self.service.is_exist.return_value = True
        assert self.service.is_exist(test_user_name)

    def test_create_user(self):
        name = 'test_user'
        user = User(username=name, password_hash=123456, email='jetqin@yahoo.com')
        self.service.create_user.return_value = {'name': 'admin', 'email': 'admin@example.com'}
        self.service.create_user(user)
        assert self.service.create_user.called_once()

    def tearDown(self) -> None:
        print("Tear down")


