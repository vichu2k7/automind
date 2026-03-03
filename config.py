"""
System configuration
"""

# BUG 2: None instead of int (causes config validation to break entirely)
# Set a sensible default capacity for users
MAX_USERS = 5  # previously None, must be positive integer

SYSTEM_NAME = "User Allocation System v2.0"

# System limits
MIN_USERS = 0
DEFAULT_CAPACITY = 100

# BUG 3: Unused config that might cause issues
DEBUG_MODE = True
