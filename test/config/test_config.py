import pytest


def test_profile(app):
    assert app.config['PROFILE'] == 'test'