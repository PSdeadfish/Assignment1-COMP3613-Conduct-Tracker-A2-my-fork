from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    is_positive = db.Column(db.Boolean, nullable=False)

    def __init__(self, student_id, comment, is_positive):
        self.student_id = student_id
        self.comment = comment
        self.is_positive = is_positive

    def get_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'comment': self.comment,
            'is_positive': self.is_positive
        }