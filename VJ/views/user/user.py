from flask import (  # noqa
    request,
    redirect,
    url_for,
    flash,
    current_app,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user, login_required

from VJ.models import UserModel


class UserView(MethodView):

    template = 'user/user.html'

    def get(self, username):
        user = UserModel.objects.get_or_404(username=username)
        return render_template(self.template, user=user)


class FollowView(MethodView):

    @login_required
    def get(self, username):
        user = UserModel.objects(username=username).first()
        if user is None:
            flash('Invalid user.')
            return redirect(url_for('user.user', username=username))
        if current_user.is_following(user):
            flash('You are already following this user.')
            return redirect(url_for('user.user', username=username))
        current_user.follow(user)
        flash('You are now following %s.' % username)
        return redirect(url_for('user.user', username=username))


class UnFollowView(MethodView):

    @login_required
    def get(self, username):
        user = UserModel.objects(username=username).first()
        if user is None:
            flash('Invalid user.')
            return redirect(url_for('user.user', username=username))
        if not current_user.is_following(user):
            flash('You are not following this user.')
            return redirect(url_for('user.user', username=username))
        current_user.unfollow(user)
        flash('You are not following %s anymore.' % username)
        return redirect(url_for('user.user', username=username))


class FollowersView(MethodView):

    template = 'user/followers.html'

    @login_required
    def get(self, username):
        user = UserModel.objects.get_or_404(username=username)
        per_page = current_app.config['FOLLOWERS_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = user.paginate_field(
            'followers',
            page=page,
            per_page=per_page
        )
        followers = paginate.items
        return render_template(
            self.template,
            user=user,
            followers=followers,
            paginate=paginate
        )


class FollowingView(MethodView):

    template = 'user/following.html'

    @login_required
    def get(self, username):
        user = UserModel.objects.get_or_404(username=username)
        per_page = current_app.config['FOLLOWING_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = user.paginate_field(
            'following',
            page=page,
            per_page=per_page
        )
        following = paginate.items
        return render_template(
            self.template,
            user=user,
            following=following,
            paginate=paginate
        )
