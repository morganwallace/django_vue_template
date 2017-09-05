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

###
# Commands
###

def dev_frontend():
    """Shortcut for running dev frontend."""
    with prefix('cd %s' % FRONTEND):
        local('npm run dev')

