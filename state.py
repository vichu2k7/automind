"""
Shared state manager
BUG 4: Improper state management causing corruption
"""

# BUG: Global variable but imported incorrectly in other modules
user_count = 0


def increment_count():
    """Increment user count"""
    global user_count
    user_count += 1
    return user_count


def get_user_count():
    """Get current user count"""
    return user_count


def decrement_count():
    """Decrement user count, never going below zero"""
    global user_count
    if user_count > 0:
        user_count -= 1
    return user_count


def reset_state():
    """Reset state to initial"""
    global user_count
    # resetting to zero so tests and logic have a clean slate
    user_count = 0

