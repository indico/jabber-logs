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
import inspect
from jabber_logs import make_app, main

if 'JABBERLOGS_CONFIG' in os.environ:
    config = os.environ['JABBERLOGS_CONFIG']
else:
    current_folder = os.path.dirname(__file__)
    config = os.path.join(current_folder, 'settings.conf')
    if not os.path.isfile(config):
        raise Exception("Couldn't find config file")

app = make_app(config)
main(app)
