from pymongo import MongoClient

def create_collections(db):
    collections = ['faculties',
                   'schools',
                   'ues',
                   'programs',
                   'teachers',
                   'students',
                   'enrollment',
                   'administrative_staff']
 
    for collection in collections:
        if collection not in db.list_collection_names():
            db.create_collection(collection)
