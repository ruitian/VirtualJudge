# -*- coding: utf-8 -*-
from VJ import app, db
from flask.ext.script import Manager, Server, Shell

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("runserver", Server(
        use_debugger=True,
        use_reloader=True,
        host="0.0.0.0",
        port=3000
    )
)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    pass

if __name__ == '__main__':
    manager.run()
