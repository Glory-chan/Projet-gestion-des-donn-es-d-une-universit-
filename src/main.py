import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_db
from src.models import create_collections
from src.seed_data import create_fake_data
from src.queries import get_student_count_per_ue
from src.add_data import (
    add_faculty, add_school, add_program, add_ue, add_teacher, add_student, add_administrative_staff, add_enrollment
)

def main():
    db = get_db()
    create_collections(db)

    while True:
        print("\nMenu:")
        print("1. Ajouter une faculté")
        print("2. Ajouter une école")
        print("3. Ajouter un programme")
        print("4. Ajouter une unité d'enseignement (UE)")
        print("5. Ajouter un enseignant")
        print("6. Ajouter un étudiant")
        print("7. Ajouter un membre du personnel administratif")
        print("8. Ajouter une inscription")
        print("9. Voir le nombre d'étudiants inscrits par UE")
        print("0. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            name = input("Nom de la faculté: ")
            description = input("Description: ")
            add_faculty(name, description)
        elif choice == '2':
            name = input("Nom de l'école: ")
            description = input("Description: ")
            add_school(name, description)
        elif choice == '3':
            name = input("Nom du programme: ")
            faculty_name = input("Nom de la faculté: ")
            school_name = input("Nom de l'école (laisser vide si non applicable): ")
            add_program(name, faculty_name, school_name)
        elif choice == '4':
            name = input("Nom de l'UE: ")
            description = input("Description: ")
            faculty_name = input("Nom de la faculté: ")
            school_name = input("Nom de l'école (laisser vide si non applicable): ")
            add_ue(name, description, faculty_name, school_name)
        elif choice == '5':
            name = input("Nom de l'enseignant: ")
            email = input("Email: ")
            faculty_name = input("Nom de la faculté: ")
            school_name = input("Nom de l'école (laisser vide si non applicable): ")
            add_teacher(name, email, faculty_name, school_name)
        elif choice == '6':
            name = input("Nom de l'étudiant: ")
            email = input("Email: ")
            program_name = input("Nom du programme: ")
            add_student(name, email, program_name)
        elif choice == '7':
            name = input("Nom du personnel administratif: ")
            email = input("Email: ")
            faculty_name = input("Nom de la faculté: ")
            school_name = input("Nom de l'école (laisser vide si non applicable): ")
            add_administrative_staff(name, email, faculty_name, school_name)
        elif choice == '8':
            student_name = input("Nom de l'étudiant: ")
            ue_name = input("Nom de l'UE: ")
            semester = input("Semestre: ")
            add_enrollment(student_name, ue_name, semester)
        elif choice == '9':
            student_counts = get_student_count_per_ue(db)
            for record in student_counts:
                print(f"UE: {record['UE']}, Nombre d'étudiants: {record['student_count']}")
        elif choice == '0':
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
