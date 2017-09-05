from fabric.api import local
from fabric.context_managers import prefix
import os


###
#  Constants
###

# Paths
ROOT = os.path.join('/', 'Users', 'morgan', 'Developer', 'my-project')
VENV_PATH = os.path.join(ROOT, 'venv', 'bin', 'activate')
FRONTEND = os.path.join(ROOT, 'frontend')
BACKEND = os.path.join(ROOT, 'backend')

###
# Commands
###

def dev_frontend():
    """Shortcut for running dev frontend."""
    with prefix('cd %s' % FRONTEND):
        local('npm run dev')

def server():
    """Shortcut for running server locally."""
    with prefix('cd %s' % BACKEND):
        with prefix('source %s' % VENV_PATH):
            local('python manage.py runserver')
