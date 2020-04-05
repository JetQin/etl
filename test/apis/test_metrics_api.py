import pytest


def test_health(client):
    """Start with a blank database."""

    rv = client.get('/api/v1/health/')
    assert rv.json['status'] == 'success'