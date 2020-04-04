import unittest
import pytest
from unittest.mock import Mock
from model import User
from service import UserService


@pytest.mark.usefixtures("logger")
class TestUserService(unittest.TestCase):

    def setUp(self) -> None:
        assert hasattr(self, "logger")
        self.logger.info("start setup")
        self.service = UserService()

    # def test_exist(self):
    #     name = 'test_user'
    #     user = User(username=name, password_hash=123456, email='jetqin@yahoo.com')
    #     self.service.create_user(user)
    #     self.assertTrue(self.service.is_exist(name), 'user should exist in database')

    def tearDown(self) -> None:
        self.logger.info("Tear down")


