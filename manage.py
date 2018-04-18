# flask
from flask_script import Manager

# application
from application.index import app, db
from application.config import config_map
from application.web.web_controller import web

manager = Manager(app)

@manager.command
def dev():
    """application will be operation in dev mode"""
    app.config.from_object(config_map['dev'])
    app.register_blueprint(web, url_prefix='/')
    db.create_all()
    app.run()

@manager.command
def prod():
    """application will be operation in prod mode"""
    app.config.from_object(config_map['prod'])
    app.register_blueprint(web, url_prefix='/')
    db.create_all()
    app.run()

if __name__ == '__main__':
    manager.run()