from VJ import db
from datetime import datetime

class ContestModel(db.Document):
    title = db.StringField()
    password = db.StringField()
    description = db.StringField()
    problems = db.ListField()
    start_at = db.DateTimeField(required=True)
    end_at = db.DateTimeField(required=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)
