from src.database import get_db
from src.models import create_collections

def test_create_collections():
    db = get_db()
    create_collections(db)
    collections = db.list_collection_names()
    assert 'faculties' in collections
    assert 'students' in collections
