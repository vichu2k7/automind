"""
User management module
"""

from state import increment_count, get_user_count

users = []


def add_user():
    """Add a new user and update global state.

    The analytics import is done inside the function to avoid a
    circular dependency at import time.
    """
    # increment the shared user count and use the returned id
    user_id = increment_count()
    users.append(f"User_{user_id}")

    # import inside function to break circular reference with module_b
    from module_b import log_analytics
    log_analytics("user_added", user_id)

    return user_id


def get_user_list():
    """Get list of all users"""
    return users


def remove_user(user_id):
    """Remove a user and update shared state counter"""
    from state import decrement_count

    if 1 <= user_id <= len(users):
        users.pop(user_id - 1)
        decrement_count()
        return True
    return False

