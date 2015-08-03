from VJ import db
from datetime import datetime
from mongoengine import DENY


class ContestProblemModel(db.EmbeddedDocument):
    problem = db.ReferenceField(
        'ProblemItem',
        dbref=True
    )
    origin_oj = db.StringField(max_length=255)
    problem_id = db.StringField(max_length=255)
    index = db.StringField(max_length=255)
    title = db.StringField(max_length=255)
    accepted = db.IntField(default=0)
    submit = db.IntField(default=0)


class ContestModel(db.Document):
    id = db.SequenceField(primary_key=True)
    title = db.StringField(max_length=255)
    contest_type = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    problems = db.ListField(
        db.EmbeddedDocumentField(
            ContestProblemModel,
        ),
        default=[]
    )
    manager = db.ReferenceField(
        'UserModel',
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
            contest_type,
            password,
            start_at,
            end_at,
            description, **kwargs):
        return cls.objects.create(
            title=title,
            contest_type=contest_type,
            password=password,
            start_at=start_at,
            end_at=end_at,
            description=description,
            **kwargs
        )
