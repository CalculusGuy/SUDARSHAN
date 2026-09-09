# validator/checks/__init__.py
from .ssti import validate_ssti
from .sqli import validate_sqli
from .xss import validate_xss
