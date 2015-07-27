from VJ import db


class ProblemItem(db.Document):
    origin_oj = db.StringField()
    problem_id = db.StringField()
    problem_url = db.StringField()
    title = db.StringField()
    time_limit = db.StringField()
    memory_limit = db.StringField()
    description = db.StringField()
    input = db.StringField()
    output = db.StringField()
    sample_input = db.StringField()
    sample_output = db.StringField()
    hint = db.StringField()
    source = db.StringField()
    update_time = db.StringField()
    accept = db.StringField()
    submit = db.StringField()

    def __unicode__(self):
        return '%s: %s' % (self.origin_oj, self.problem_id)

    meta = {
        'collection': 'ProblemItem',
        'indexes': ['origin_oj', 'problem_id']
    }
