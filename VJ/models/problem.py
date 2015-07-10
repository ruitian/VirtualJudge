from VJ import db
from datetime import datetime

class ProblemItem(db.Document):
    origin_oj = db.StringField()
    problem_id = db.StringField()
    problem_url = db.StringField()
    title = db.StringField()
    time_limit = db.StringField()
    memory_limit = db.StringField()
    description = db.StringField()
    input = db.StringField()
    ouput = db.StringField()
    sample_input = db.StringField()
    sample_output = db.StringField()
    hint = db.StringField()
    source = db.StringField()
