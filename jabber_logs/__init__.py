# -*- coding: utf-8 -*-
##
##
## This file is part of Jabber Logs
## Copyright (C) 2014 European Organization for Nuclear Research (CERN)
##
## Jabber Logs is free software: you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## Jabber Logs is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Jabber Logs.  If not, see <http://www.gnu.org/licenses/>.


import os
from flask import Flask

app = Flask(__name__)


def setup_blueprints(app):
    from jabber_logs.views import log_views
    app.register_blueprint(log_views)


def make_app(config_file):
    app.config.from_pyfile(os.path.join(os.getcwd(), config_file))
    app.debug = app.config.get('DEBUG', False)
    setup_blueprints(app)
    return app


def main(application):
    application.run(host=app.config.get('SERVER_HOST', 'localhost'),
                    port=int(app.config.get('SERVER_PORT', 5000)))
