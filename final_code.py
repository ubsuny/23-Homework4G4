import math
from module_file import *
#import unittest

class TestCalculatePeriodicTime(unittest.TestCase):
    def test_calculate_periodic_time(self):
        # Define a list of lengths of pendulums
        x = [0.5, 1, 1.5, 2, 2.5]

        # Expected periodic times using the correct formula, adjusted for better precision
        expected_periodic_times = [1.4185, 2.006, 2.451, 2.828, 3.162]

        # Use the calculate_periodic_time() function to calculate the periodic times
        actual_p_t = list(map(calculate_periodic_time, x))

        # Print and assert that the actual periodic times are close to the expected periodic times
        for i, length in enumerate(x):
            print(f"For l = {length}, Expected: {expected_periodic_times[i]}, Got: {actual_p_t[i]}")
            assert math.isclose(actual_p_t[i], expected_periodic_times[i], rel_tol=1e-2)
            
 if __name__ == '__main__':
     unittest.main(argv=['first-arg-is-ignored'], exit=False)

