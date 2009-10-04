#!/usr/bin/env python
import sys
import os
sys.path.insert(0, '.')
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pkg_resources import require
require("django>=1.1")

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)