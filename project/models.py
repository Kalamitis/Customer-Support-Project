from datetime import datetime
from project import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    customer = db.Column(db.Text, nullable=False)
    microscope = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    date_req = db.Column(db.Text, nullable=False)
    problem_disc = db.Column(db.Text, nullable=False)
    os = db.Column(db.Text, nullable=False)
    digistar = db.Column(db.Text, nullable=False)
    gis = db.Column(db.Text, nullable=False)
    people_inv = db.Column(db.Text, nullable=False)
    actions = db.Column(db.Text, nullable=False)
    spares = db.Column(db.Text, nullable=False)
    date_fix = db.Column(db.Text, nullable=False)
    warranty = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
