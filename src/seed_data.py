from faker import Faker
import random
from bson.objectid import ObjectId
from src.database import get_db

fake = Faker()

def create_fake_data(db, num_faculties=5, num_schools=1, num_programs=10, num_ues=50, num_teachers=20, num_students=100, num_staff=10):
    faculties = []
    for _ in range(num_faculties):
        faculty = {
            'name': fake.company(),
            'description': fake.catch_phrase()
        }
        faculties.append(faculty)
    db.faculties.insert_many(faculties)

    schools = []
    for _ in range(num_schools):
        school = {
            'name': fake.company(),
            'description': fake.catch_phrase()
        }
        schools.append(school)
    db.schools.insert_many(schools)

    programs = []
    for _ in range(num_programs):
        program = {
            'name': fake.job(),
            'faculty_id': random.choice(faculties)['_id'],
            'school_id': random.choice(schools)['_id'] if schools else None
        }
        programs.append(program)
    db.programs.insert_many(programs)

    ues = []
    for _ in range(num_ues):
        ue = {
            'name': fake.bs(),
            'description': fake.text(),
            'faculty_id': random.choice(faculties)['_id'],
            'school_id': random.choice(schools)['_id'] if schools else None
        }
        ues.append(ue)
    db.ues.insert_many(ues)

    teachers = []
    for _ in range(num_teachers):
        teacher = {
            'name': fake.name(),
            'email': fake.email(),
            'faculty_id': random.choice(faculties)['_id'],
            'school_id': random.choice(schools)['_id'] if schools else None
        }
        teachers.append(teacher)
    db.teachers.insert_many(teachers)

    students = []
    for _ in range(num_students):
        student = {
            'name': fake.name(),
            'email': fake.email(),
            'program_id': random.choice(programs)['_id']
        }
        students.append(student)
    db.students.insert_many(students)

    staff = []
    for _ in range(num_staff):
        admin_staff = {
            'name': fake.name(),
            'email': fake.email(),
            'faculty_id': random.choice(faculties)['_id'],
            'school_id': random.choice(schools)['_id'] if schools else None
        }
        staff.append(admin_staff)
    db.administrative_staff.insert_many(staff)

    enrollments = []
    for student in students:
        for _ in range(random.randint(1, 5)):
            enrollment = {
                'student_id': student['_id'],
                'ue_id': random.choice(ues)['_id'],
                'semester': random.choice(['Fall', 'Spring', 'Summer'])
            }
            enrollments.append(enrollment)
    db.enrollment.insert_many(enrollments)

if __name__ == "__main__":
    db = get_db()
    create_fake_data(db)
