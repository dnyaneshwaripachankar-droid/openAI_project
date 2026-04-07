"""
Utils Package
A collection of helper modules for [Project Name].
"""

__version__ = "0.1.0"

# 1. Flatten the API: Expose main functions from sub-modules
# This allows "from utils import helper_func" instead of 
# "from utils.helpers import helper_func"
try:
    from .helpers import format_timestamp, slugify_text
    from .validators import is_valid_email, validate_config
    from .logger import get_logger
except ImportError as e:
    # Optional: Log the error or handle missing dependencies
    # This prevents the whole app from crashing if one utility has a missing requirement
    print(f"Warning: Some utilities could not be loaded: {e}")

# 2. Define the public API for the package
# This controls what is exported when someone runs 'from utils import *'
__all__ = [
    'format_timestamp',
    'slugify_text',
    'is_valid_email',
    'validate_config',
    'get_logger'
]

# 3. Initialization Logic (Optional)
# This code runs the first time the package is imported
_logger = get_logger(__name__)
_logger.debug("Utils package initialized successfully.")