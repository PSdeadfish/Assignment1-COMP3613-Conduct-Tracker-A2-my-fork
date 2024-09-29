from App.models import Student, Review
from App.database import db

def add_student(name):
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_student_by_name(name):
    return Student.query.filter_by(name=name).first()

def get_student(student_id):
    return Student.query.get(student_id)

def get_all_students():
    return Student.query.all()

def add_review(student_id, comment, is_positive):
    new_review = Review(student_id=student_id, comment=comment, is_positive=is_positive)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def get_reviews_for_student(student_id):
    student = get_student(student_id)
    if student:
        return student.reviews
    return []
