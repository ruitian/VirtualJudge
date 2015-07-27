from VJ import db
from datetime import datetime

from base64 import b64encode


class SolutionItem(db.Document):
    solution_id = db.SequenceField()
    origin_oj = db.StringField()
    problem_id = db.StringField()
    username = db.StringField()
    run_id = db.StringField()
    source = db.StringField()
    result = db.StringField(default="Queuing && Judging")
    memory = db.StringField()
    time = db.StringField()
    language = db.StringField()
    code_length = db.StringField()
    submit_time = db.StringField()
    created_at = db.DateTimeField(default=datetime.now, required=True)

    meta = {
        'collection': 'SolutionItem',
        'indexes': ['id', 'origin_oj', 'problem_id']
    }

    @staticmethod
    def generate_source(code):
        return b64encode(code)

    @classmethod
    def create_solution(
            cls,
            origin_oj,
            problem_id,
            username,
            language,
            code, **kwargs):
        source = cls.generate_source(code)
        return cls.objects.create(
            origin_oj=origin_oj,
            problem_id=problem_id,
            username=username,
            language=language,
            source=source,
            **kwargs
        )
