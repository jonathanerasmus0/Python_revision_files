#postgres and dJango

import os

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    import django
    django.setup()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    