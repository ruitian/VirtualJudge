from VJ import db
from datetime import datetime
from VJ.models.problem import ProblemItem
from mongoengine import DENY, NULLIFY

class ContestModel(db.Document):
    id = db.SequenceField(primary_key=True)
    title = db.StringField()
    password = db.StringField()
    description = db.StringField()
    problems = db.ListField(
        db.ReferenceField(
            ProblemItem,
            reverse_delete_rule=DENY
        )
    )
    start_at = db.DateTimeField(required=True)
    end_at = db.DateTimeField(required=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)
