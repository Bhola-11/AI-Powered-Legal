#!/usr/bin/env python
"""
CivicLaw Platform - Main Application Entrypoint
AI-Powered Legal Case Management & Court Workflow Platform
"""
import os
import sys

def main():
    """Run administrative or web server tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Default to running development server if no arguments provided
    args = sys.argv if len(sys.argv) > 1 else [sys.argv[0], "runserver", "0.0.0.0:8000"]
    execute_from_command_line(args)

if __name__ == "__main__":
    main()
