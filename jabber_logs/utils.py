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


def select_file(fDate, sDate, eDate):
    if sDate and eDate:
        # both specified, compare with the two limits
        return fDate >= sDate and fDate <= eDate
    elif sDate and not eDate:
        # only one specified
        return fDate >= sDate
    elif not sDate and eDate:
        return fDate <= eDate
    else:
        # no limits, we add all
        return True


def get_dir_name(logsPath, cr, number):
    if os.path.exists(os.path.join(logsPath, "{0}.{1}".format(cr, number))):
        number = get_dir_name(logsPath, cr, number+1)
    return number
