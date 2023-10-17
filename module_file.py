# module
import unittest
import math

def calculate_periodic_time(l):
    """Calculates the periodic time of a simple pendulum.

    Args:
      l: The length of the pendulum in meters.

    Returns:
      The periodic time of the pendulum in seconds.
    """
    # Acceleration due to gravity in meters per second squared.
    g = 9.81
    
    # Correct formula for the period of a simple pendulum
    return 2 * math.pi * math.sqrt(l / g)
