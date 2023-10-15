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
# use lambda function calculate the periodic time where l is the length of the string and return the value calculated
  calculate_periodic_time= (lambda l: 2* math.pi/ math.sqrt(g / l))
  return calculate_periodic_time
  
__all__=["calculate_periodic_time"]

lengths_list = [1,2,3,4]
  # Split the user input string into a list.
#lengths_list = lengths_list.split(",")
  # Convert the elements of the list to integers
integer_list = []
for element in lengths_list:
   integer_list.append(float(element))
    # Print the integer list.
print("your list of lengths is: ", integer_list,"meters")
    #--------------------------------------------------------------#
    # Use map to apply the lambda function to each length in the list
periodic_times = map(calculate_periodic_time(integer_list), integer_list)
    # Print the periodic times and round them to 2 sig digits
T=[periodic_time for periodic_time in periodic_times]
round_time=[round(element,2) for element in T]
print("periodic times corresporing to the lengths are ", round_time,"seconds")

__all__=["period"]
