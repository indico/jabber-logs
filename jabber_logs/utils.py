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
