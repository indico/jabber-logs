import os
from flask import Flask

app = Flask(__name__)


def setup_blueprints(app):
    from jappix_logs.views import log_views
    app.register_blueprint(log_views)


def make_app(config_file):
    app.config.from_pyfile(os.path.join(os.getcwd(), config_file))
    app.debug = app.config.get('DEBUG', False)
    setup_blueprints(app)
    return app

def main(application):
    application.run(host=app.config.get('SERVER_HOST', 'localhost'),
                    port=int(app.config.get('SERVER_PORT', 5000)))
