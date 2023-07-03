from .. import db
from .user import User


class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    questions = db.Column(db.JSON)
    answers = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship(User, backref=db.backref('quizzes', lazy='True'))


class Score(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship(User, backref=db.backref('scores', lazy='True'))

