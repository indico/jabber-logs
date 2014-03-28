import os
import re
import string
import errno
import dateutil.parser
from datetime import datetime, date
from flask import Blueprint, json, request, jsonify, current_app as app

from jabber_logs.utils import select_file, get_dir_name

log_views = Blueprint('views', __name__)


@log_views.route('/')
def getLog():

    # get the range of dates to pick logs
    params = request.args
    try:
        name = params['cr']
    except KeyError:
        return jsonify(success=False, error='Chat room name not specified')

    if 'sdate' in params:
        sDate = dateutil.parser.parse(params.get('sdate'))
        print sDate
    else:
        sDate = None

    if 'edate' in params:
        eDate = dateutil.parser.parse(params.get('edate'))
    else:
        eDate = None

    logsPath = app.config.get('LOG_PATH', "")
    try:
        files = os.listdir(logsPath + name)
    except Exception, e:
        # file doesn't exist in our server, someone deleted it manually
        return jsonify(success=False, error='Chat room name not found')

    filesToFetch = []
    for file in files:
        fDate = dateutil.parser.parse(string.replace(file, '.html', ''))
        # we add it to the list if it's in the range of dates or there's no range specified
        if select_file(fDate, sDate, eDate):
            filesToFetch.append(fDate)

    # order the result and transform the dates into strings with the file name
    result = ''
    filesToFetch.sort()
    for item in filesToFetch:
        file_name = "{0}.html".format(item.date())
        with open('{0}/{1}'.format(logsPath + name, file_name), 'r') as file:
            result += file.read()
    return result


@log_views.route('/delete')
def deleteDir():
    try:
        cr = request.args['cr']
    except KeyError:
        return jsonify(success=False, error='Chat room name not specified')

    logsPath = app.config.get('LOG_PATH', False)

    newNumber = get_dir_name(logsPath, cr, 0)
    try:
        os.rename("{0}{1}".format(logsPath, cr), "{0}{1}.{2}".format(logsPath, cr, newNumber))
    except OSError, e:
        # The directory is not there. Maybe some other request changed its name
        # quite at the same time, or maybe someone deleted the file manually.
        # In any case, there's nothing to change in this case
        if e.errno == errno.ENOENT:
            return jsonify(success=False, error='The chat has been previously deleted')
    return jsonify(success=True)
