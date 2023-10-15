import algorithm
lengths_list = input("Enter a list of length, separated by commas: ")
  # Split the user input string into a list.
lengths_list = lengths_list.split(",")
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
    
