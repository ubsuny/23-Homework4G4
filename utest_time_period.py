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

  # Use lambda function calculate the periodic time where l is the length of the string and return the value calculated
  calculate_periodic_time = (lambda l: 2 * math.pi / math.sqrt(g / l))
  return calculate_periodic_time

class TestCalculatePeriodicTime(unittest.TestCase):

  def test_calculate_periodic_time(self):
    # Define a list of lengths of pendulums
    x = [0.5, 1, 1.5, 2, 2.5]

    # Calculate the expected periodic times
    expected_periodic_times = [1.57, 3.14, 4.44, 5.66, 6.84]

    # Use the calculate_periodic_time() function to calculate the periodic times
    actual_periodic_times = map(calculate_periodic_time, x)

    # Assert that the actual periodic times are equal to the expected periodic times
    for i in range(len(x)):
      assert actual_periodic_times[i] == expected_periodic_times[i]

if __name__ == '__main__':
  unittest.main()
  #Instead of the above two lines, we can use, two lines, below too.
#if __name__ == '__main__':
 # unittest.main(argv=['first-arg-is-ignored'], exit=False)
