#!/usr/bin/env python
"""
CivicLaw Application WSGI / Web Runner Entry Point
"""
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    from config.wsgi import application
    app = application
except Exception:
    app = None

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    args = sys.argv if len(sys.argv) > 1 else [sys.argv[0], "runserver", "0.0.0.0:8000"]
    execute_from_command_line(args)
