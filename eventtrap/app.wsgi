import os, sys
sys.path.append('/opt/projects/eventtrap/eventtrap')
sys.path.append('/opt/projects/eventtrap/venv/lib/python2.7/site-packages')
activate_env=os.path.expanduser('/opt/projects/eventtrap/venv/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))
from app import app as application
