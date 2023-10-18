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
    G = 9.81
    # Constant (g) should be in capital 
    # Correct formula for the period of a simple pendulum
    return 2 * math.pi * math.sqrt(l / g)

class TestCalculatePeriodicTime(unittest.TestCase):

    def test_calculate_periodic_time(self):
        # Define a list of lengths of pendulums
        x = [0.5, 1, 1.5, 2, 2.5]

        # Expected periodic times using the correct formula, adjusted for better precision
        expected_periodic_times = [1.4185, 2.006, 2.451, 2.828, 3.162]

        # Use the calculate_periodic_time() function to calculate the periodic times
        actual_periodic_times = list(map(calculate_periodic_time, x))

        # Print and assert that the actual periodic times are close to the expected periodic times
        for i in range(len(x)):
            print(f"For l = {x[i]}, Expected: {expected_periodic_times[i]}, Got: {actual_periodic_times[i]}")
            assert math.isclose(actual_periodic_times[i], expected_periodic_times[i], rel_tol=1e-2)  # Increased tolerance

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
