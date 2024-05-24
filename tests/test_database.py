import pytest
from src.database import get_db

def test_db_connection():
    db = get_db()
    assert db.name == 'university'
