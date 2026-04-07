"""
Utilities Module
This module provides shared helper functions and classes across the application.
"""

# Import specific functions from sub-modules to expose them at the package level
try:
    from .helpers import (
        format_date,
        clean_string,
        slugify
    )
except ImportError:
    format_date = None
    clean_string = None
    slugify = None

try:
    from .validators import validate_email, validate_config
except ImportError:
    validate_email = None
    validate_config = None

try:
    from .logger import setup_custom_logger
except ImportError:
    setup_custom_logger = None

# Define what is accessible when someone uses 'from utils import *'
__all__ = [
    'format_date',
    'clean_string',
    'slugify',
    'validate_email',
    'validate_config',
    'setup_custom_logger'
]

__version__ = "1.0.0"