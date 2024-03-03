#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import firebase_admin
from firebase_admin import credentials

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    cred = credentials.Certificate("\task-app-b58f4-firebase-adminsdk-2pkh6-39b7c7a042.json")
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL': databaseURL,
    })


if __name__ == '__main__':
    main()
