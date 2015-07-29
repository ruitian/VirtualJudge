from flask import (  # noqa
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView

from VJ.models import UserModel


class UserView(MethodView):

    template = 'user/user.html'

    def get(self, username):
        user = UserModel.objects.get_or_404(username=username)
        return render_template(self.template, user=user)
