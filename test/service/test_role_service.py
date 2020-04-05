import pytest
import unittest
from unittest.mock import Mock, MagicMock
from model import Role
from service import RoleService


class TestRoleService(unittest.TestCase):

    def setUp(self) -> None:
        self.service = Mock(spec=RoleService)
        self.role = Role(name='test_admin', description='test')

    def test_create_role(self):
        self.service.create_role.return_value = {'name': 'test_admin', 'description': 'test'}
        result = self.service.create_role(self.role)
        self.service.create_role.assert_called_once()
        assert result['name'] == 'test_admin'

    def test_list_role(self):
        self.service.list_role.return_value = [self.role.as_dict()]
        result = self.service.list_role()
        self.service.list_role.assert_called_once()
        assert len(result) == 1
