from VJ import db
from datetime import datetime
from flask.ext.security import UserMixin

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)
