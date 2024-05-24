from src.database import get_db
from src.seed_data import create_fake_data

def test_create_fake_data():
    db = get_db()
    create_fake_data(db, num_faculties=1, num_schools=1, num_programs=1, num_ues=1, num_teachers=1, num_students=1, num_staff=1)
    assert db.faculties.count_documents({}) == 1
    assert db.schools.count_documents({}) == 1
    assert db.programs.count_documents({}) == 1
    assert db.ues.count_documents({}) == 1
    assert db.teachers.count_documents({}) == 1
    assert db.students.count_documents({}) == 1
    assert db.administrative_staff.count_documents({}) == 1
    assert db.enrollment.count_documents({}) >= 1
