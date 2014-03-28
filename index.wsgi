import os
import inspect
from jappix_logs import make_app, main

if 'JAPPIXLOGS_CONFIG' in os.environ:
    config = os.environ['JAPPIXLOGS_CONFIG']
else:
    current_folder = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    config = os.path.join(current_folder, 'settings.conf')
    if not os.path.isfile(config):
        raise Exception("Couldn't find config file")

application = make_app(config)
