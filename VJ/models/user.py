from VJ import db, login_manager
from datetime import datetime
from flask.ext.security import UserMixin
from flask.ext.security.utils import encrypt_password
from flask.ext.security.utils import verify_password as _verify_password
from VJ.models.role import RoleModel
from flask import current_app
from mongoengine import DENY

@login_manager.user_loader
def load_user(id):
    User.objects(_id=id)

class UserModel(db.Document, UserMixin):
    username = db.StringField(max_length=255)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    roles = db.ListField(
        db.ReferenceField(RoleModel, reverse_delete_rule=DENY),
        default=[]
    )

    active = db.BooleanField(default=True)

    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=255)
    current_login_ip = db.StringField(max_length=255)

    @staticmethod
    def generate_password(password):
        return encrypt_password(
            current_app.config['SECRET_KEY'] + password
        )

    def set_password(self, password):
        self.password = generate_password(password)

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        password = cls.generate_password(password)
        return cls.objects.create(
            username = username,
            email = email,
            password = password,
            **kwargs
        )

    def verify_password(self, password):
        return _verify_password(
            self.password,
            current_app.config['SECRET_KEY'] + password
        )

    def __unicode__(self):
        return self.email
