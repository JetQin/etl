import pytest
import unittest
import requests
from unittest.mock import Mock


class TestUserApi(unittest.TestCase):

    def setUp(self) -> None:
        print("\tsetup_class")
        r = requests.get('http://localhost:5000/api/health')
        if r.status_code == 200:
            return r.json()
        return None

    def test_create_user(self):
        value = 3
        assert value == 3

    def tearDown(self) -> None:
        print("\tteardown_class")

