
from .db import db
import mongoengine_goodjson as gj
from flask_bcrypt import generate_password_hash, check_password_hash

# class Movie(db.Document):
class Movie(gj.Document):
    """
    This changes the format to GoodJSON
    """
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')

class User(gj.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
 
    def check_password(self, password):
        return check_password_hash(self.password, password)

#  User.register_delete_rule(Movie, 'added_by', db.CASCADE) creates another delete rule which means if a user is deleted then the movie created by the user is also deleted. 
# User.register_delete_rule(Movie, 'added_by', db.CASCADE) 