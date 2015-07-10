from VJ import db
from datetime import datetime
from flask.ext.security import RoleMixin

class RoleModel(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)

    def __unicode__(self):
        return self.name
