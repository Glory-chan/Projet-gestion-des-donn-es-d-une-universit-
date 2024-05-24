from bson.objectid import ObjectId

def get_student_count_per_ue(db):
    pipeline = [
        {
            '$group': {
                '_id': '$ue_id',
                'student_count': {'$sum': 1}
            }
        },
        {
            '$lookup': {
                'from': 'ues',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'ue_info'
            }
        },
        {
            '$unwind': '$ue_info'
        },
        {
            '$project': {
                '_id': 0,
                'UE': '$ue_info.name',
                'student_count': 1
            }
        }
    ]
    return list(db.enrollment.aggregate(pipeline))

def get_ues_by_faculty(db, faculty_id):
    return list(db.ues.find({'faculty_id': ObjectId(faculty_id)}))

def get_students_by_program(db, program_id):
    return list(db.students.find({'program_id': ObjectId(program_id)}))
