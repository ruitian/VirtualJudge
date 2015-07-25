from VJ import db
from datetime import datetime

class RoleModel(db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)

    def __unicode__(self):
        return self.name
