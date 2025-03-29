
import sys
import os

path = "/home/yan-albuquerque/Sistema-de-Estoque"
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()