from src.database import get_db
from src.queries import get_student_count_per_ue

def test_get_student_count_per_ue():
    db = get_db()
    results = get_student_count_per_ue(db)
    assert len(results) > 0
