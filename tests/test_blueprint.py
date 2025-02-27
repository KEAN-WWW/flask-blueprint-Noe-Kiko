"""This is a test script to test flask application"""
from application.app import app


def test_bp_usage():
    """Test if there is blueprint registered"""
    assert app.blueprints.keys(), "No Blueprint Registered!"
