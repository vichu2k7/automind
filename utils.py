"""
Utility functions
"""

from config import MAX_USERS


def calculate_capacity(current, maximum):
    """
    Check if system has capacity for more users
    The function should return True when there is still room (current < maximum)
    and False when the limit has been reached or exceeded.
    """
    return current < maximum



def validate_user_id(user_id):
    """Validate user ID is positive"""
    return user_id > 0


def get_max_capacity():
    """Return maximum capacity"""
    return MAX_USERS


# hidden bonus calculator is simplified to avoid divide-by-zero
# and still return a deterministic value for bonuses
def hidden_bonus_calculator(x):
    """Unused function adjusted to return a safe value"""
    return x * 2  # simple example, avoids any division


# BUG 7: Another hidden issue
def inefficient_function(data):
    """Unused inefficient implementation"""
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                result.append(data[i])
    return result
