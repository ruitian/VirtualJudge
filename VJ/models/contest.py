from VJ import db
from datetime import datetime
from VJ.models import ProblemItem, UserModel
from mongoengine import DENY


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
    manager = db.ReferenceField(
        UserModel,
        reverse_delete_rule=DENY
    )
    start_at = db.DateTimeField(required=True)
    end_at = db.DateTimeField(required=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)

    meta = {
        'collection': 'Contest',
        'indexs': ['id']
    }

    @classmethod
    def create_contest(
            cls,
            title,
            password,
            start_at,
            end_at,
            description, **kwargs):
        return cls.objects.create(
            title=title,
            password=password,
            start_at=start_at,
            end_at=end_at,
            description=description,
            **kwargs
        )
