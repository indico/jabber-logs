import os, re, string
import dateutil.parser
from datetime import datetime, date
from flask import Blueprint, json, request, Response, current_app as app

log_views = Blueprint('views', __name__, template_folder='templates')

@log_views.route('/', methods=['GET'])
def getLog():
    def _selectFile(fDate, sDate, eDate):
        if sDate and eDate:
            # both specified, compare with the two limits
            if fDate >= sDate and fDate <= eDate:
                return True
            else:
                return False
        elif sDate and not eDate:
            # only one specified
            if fDate >= sDate:
                return True
            else:
                return False
        elif not sDate and eDate:
            if fDate <= eDate:
                return True
            else:
                return False
        else:
            # no limits, we add all
             return True
    # get the range of dates to pick logs
    params = request.args

    if 'cr' in params:
        name = params.get('cr')
    else:
        return 'Chat room name not specified'

    if 'sdate' in params:
        sDate = dateutil.parser.parse(params.get('sdate'))
    else:
        sDate = None

    if 'sdate' in params:
        eDate = dateutil.parser.parse(params.get('edate'))
    else:
        eDate = None

    logsPath = app.config.get('LOG_PATH', "")
    try:
        print logsPath + name
        files = os.listdir(logsPath + name)
    except Exception, e:
        # file doesn't exist in our server, someone deleted it manually
        return 'Chat room name not found'
    filesToFetch = []
    for file in files:
        fDate = dateutil.parser.parse(string.replace(file, '.html', ''))
        # we add it to the list if it's in the range of dates or there's no range specified
        if _selectFile(fDate, sDate, eDate):
            filesToFetch.append(fDate)

    # order the result and transform the dates into strings with the file name
    result = ''
    filesToFetch.sort()
    for item in filesToFetch:
        file_name = "{0}.html".format(item.date())
        file = open('{0}/{1}'.format(logsPath + name, file_name), 'r')
        result += file.read()
    return result


@log_views.route('/delete', methods=['GET'])
def deleteDir():
    def _getDirName(logsPath, cr, number):
        if os.path.exists(os.path.join(logsPath, "{0}.{1}".format(cr, number))):
            number = _getDirName(logsPath, cr, number+1)
        return number

    params = request.args
    if 'cr' in params:
        cr = params.get('cr')
    else:
        return 'Chat room name not specified'

    logsPath = app.config.get('LOG_PATH', False)

    newNumber = _getDirName(logsPath, cr, 0)
    try:
        os.rename(logsPath + cr, logsPath+cr+'.'+str(newNumber))
    except Exception, e:
        print e
        # The directory is not there. Maybe some other request changed its name
        # quite at the same time, or maybe someone deleted the file manually.
        # In any case, there's nothing to change in this case
        pass
    return "True"
