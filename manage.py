#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

AWS_SECRET_KEY="5sVuvbO367NZYBXL7lDEs1HX3Qkz33ks0qpai11/"
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRFCRUD.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
