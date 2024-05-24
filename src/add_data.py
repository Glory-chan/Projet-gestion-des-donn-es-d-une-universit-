from bson.objectid import ObjectId
from src.database import get_db

def add_faculty(name, description):
    db = get_db()
    faculty = {
        'name': name,
        'description': description
    }
    db.faculties.insert_one(faculty)

def add_school(name, description):
    db = get_db()
    school = {
        'name': name,
        'description': description
    }
    db.schools.insert_one(school)

def add_program(name, faculty_name, school_name=None):
    db = get_db()
    faculty = db.faculties.find_one({'name': faculty_name})
    if not faculty:
        print("Faculté non trouvée")
        return

    school_id = None
    if school_name:
        school = db.schools.find_one({'name': school_name})
        if not school:
            print("École non trouvée")
            return
        school_id = school['_id']

    program = {
        'name': name,
        'faculty_id': faculty['_id'],
        'school_id': school_id
    }
    result = db.programs.insert_one(program)
    print(f"Programme ajouté avec l'ID: {result.inserted_id}")

def add_ue(name, description, faculty_name, school_name=None):
    db = get_db()
    # Recherche de la faculté par son nom pour obtenir son ObjectId
    faculty = db.faculties.find_one({'name': faculty_name})
    if not faculty:
        print("Faculté non trouvée")
        return
    
    # Recherche de l'école par son nom si fourni, pour obtenir son ObjectId
    school_id = None
    if school_name:
        school = db.schools.find_one({'name': school_name})
        if not school:
            print("École non trouvée")
            return
        school_id = school['_id']
    
    # Création de l'UE avec les ObjectId récupérés
    ue = {
        'name': name,
        'description': description,
        'faculty_id': faculty['_id'],
        'school_id': school_id
    }
    result = db.ues.insert_one(ue)
    print(f"UE ajoutée avec l'ID: {result.inserted_id}")


def add_teacher(name, email, faculty_name, school_name=None):
    db = get_db()
    
    # Recherche de la faculté par son nom pour obtenir son ObjectId
    faculty = db.faculties.find_one({'name': faculty_name})
    if not faculty:
        print("Faculté non trouvée")
        return
    
    # Recherche de l'école par son nom si fourni, pour obtenir son ObjectId
    school_id = None
    if school_name:
        school = db.schools.find_one({'name': school_name})
        if not school:
            print("École non trouvée")
            return
        school_id = school['_id']
    
    # Création de l'enseignant avec les ObjectId récupérés
    teacher = {
        'name': name,
        'email': email,
        'faculty_id': faculty['_id'],
        'school_id': school_id
    }
    result = db.teachers.insert_one(teacher)
    print(f"Enseignant ajouté avec l'ID: {result.inserted_id}")


def add_student(name, email, program_name):
    db = get_db()
    program = db.programs.find_one({'name': program_name})
    if not program:
        print("Programme non trouvé")
        return

    student = {
        'name': name,
        'email': email,
        'program_id': program['_id']
    }
    result = db.students.insert_one(student)
    print(f"Étudiant ajouté avec l'ID: {result.inserted_id}")

def add_administrative_staff(name, email, faculty_name, school_name=None):
    db = get_db()
    
    # Recherche de la faculté par son nom pour obtenir son ObjectId
    faculty = db.faculties.find_one({'name': faculty_name})
    if not faculty:
        print("Faculté non trouvée")
        return
    
    # Recherche de l'école par son nom si fourni, pour obtenir son ObjectId
    school_id = None
    if school_name:
        school = db.schools.find_one({'name': school_name})
        if not school:
            print("École non trouvée")
            return
        school_id = school['_id']
    
    # Création du personnel administratif avec les ObjectId récupérés
    staff = {
        'name': name,
        'email': email,
        'faculty_id': faculty['_id'],
        'school_id': school_id
    }
    result = db.administrative_staff.insert_one(staff)
    print(f"Personnel administratif ajouté avec l'ID: {result.inserted_id}")

def add_enrollment(student_name, ue_name, semester):
    db = get_db()
    
    # Recherche de l'étudiant par son nom pour obtenir son ObjectId
    student = db.students.find_one({'name': student_name})
    if not student:
        print("Étudiant non trouvé")
        return
    
    # Recherche de l'UE par son nom pour obtenir son ObjectId
    ue = db.ues.find_one({'name': ue_name})
    if not ue:
        print("UE non trouvée")
        return
    
    # Création de l'inscription avec les ObjectId récupérés
    enrollment = {
        'student_id': student['_id'],
        'ue_id': ue['_id'],
        'semester': semester
    }
    result = db.enrollment.insert_one(enrollment)
    print(f"Inscription ajoutée avec l'ID: {result.inserted_id}")

