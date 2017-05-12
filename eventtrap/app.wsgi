import os, sys
sys.path.append('/opt/apps/eventtrap/eventtrap')
sys.path.append('/opt/apps/eventtrap/venv/lib/python2.7/site-packages')
activate_env=os.path.expanduser('/opt/apps/eventtrap/venv/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))
from app import app as application
