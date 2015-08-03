# -*- coding: utf-8 -*-

from VJ import db, login_manager
from datetime import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from VJ.models.role import RoleModel
from flask import current_app
from mongoengine import DENY, NULLIFY

from hashlib import md5
from .role import Permission


@login_manager.user_loader
def load_user(id):
    return UserModel.objects(id=id).first()


class AccountItem(db.Document):
    origin_oj = db.StringField()
    username = db.StringField(max_length=255)
    nickname = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    status = db.StringField(default='Unauthorized')
    accept = db.StringField()
    submit = db.StringField()
    rank = db.StringField()
    solved = db.DictField()

    meta = {
        'collection': 'AccountItem'
    }


class UserModel(db.Document, UserMixin):
    id = db.SequenceField(primary_key=True)
    username = db.StringField(max_length=255)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    role = db.ReferenceField(RoleModel, reverse_delete_rule=DENY)

    active = db.BooleanField(default=True)
    confirmed = db.BooleanField(default=False)

    following = db.ListField(
        db.ReferenceField(
            'UserModel',
            dbref=True
        ),
        default=[]
    )
    followers = db.ListField(
        db.ReferenceField(
            'UserModel',
            dbref=True
        ),
        default=[]
    )

    poj = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)
    hdu = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)
    sdut = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)
    fzu = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)

    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=255)
    current_login_ip = db.StringField(max_length=255)

    nickname = db.StringField(max_length=255)
    school = db.StringField(max_length=255)
    blog_url = db.StringField(max_length=255)
    location = db.StringField(max_length=255)

    @property
    def email_md5(self):
        email = self.email.strip()
        if isinstance(email, unicode):  # noqa
            email = email.encode('utf-8')
        return md5(email).hexdigest()

    def avatar(self, size=48):
        return "{0}{1}?d=mm&s={2}".format(
            current_app.config['GRAVATAR_BASE_URL'], self.email_md5, size
        )

    @staticmethod
    def generate_password(password):
        return generate_password_hash(
            current_app.config['SECRET_KEY'] + password
        )

    def set_password(self, password):
        self.password = self.generate_password(password)

    def verify_password(self, password):
        return check_password_hash(
            self.password,
            current_app.config['SECRET_KEY'] + password
        )

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        password = cls.generate_password(password)
        return cls.objects.create(
            username=username,
            email=email,
            password=password,
            **kwargs
        )

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        self.save()
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = self.generate_password(new_password)
        self.save()
        return True

    def follow(self, user):
        if not self.is_following(user):
            self.following.append(user)
            user.followers.append(self)
            self.save()
            user.save()

    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)
        self.save()
        user.save()

    def is_following(self, user):
        return user in self.following is not None

    def is_followed_by(self, user):
        return user in self.followers is not None

    def get_account(self, origin_oj):
        if origin_oj == 'poj':
            return self.poj
        elif origin_oj == 'hdu':
            return self.hdu
        elif origin_oj == 'sdut':
            return self.sdut
        elif origin_oj == 'fzu':
            return self.fzu

    def can(self, permissions):
        return (self.role and
                (self.role.permissions & permissions) == permissions)

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __unicode__(self):
        return self.email

    meta = {
        'collection': 'User'
    }
