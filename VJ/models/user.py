from VJ import db
from datetime import datetime
from flask.ext.security import UserMixin

class User(db.Document, UserMixin):
    email = db.StringField(required=True)
    password = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])
