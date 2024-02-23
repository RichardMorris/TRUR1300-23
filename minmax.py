# A function to calculate the minimum and maximum values in a list

def minmax(data):
    # Initialize the minimum and maximum values
    minval = data[0]
    maxval = data[0]

    # Loop over the data
    for val in data:
        # If the current value is less than the minimum, set it as the minimum
        if val < minval:
            minval = val
        # If the current value is greater than the maximum, set it as the maximum
        if val > maxval:
            maxval = val

    # Return the minimum and maximum values
    return minval, maxval

def sum(data):
    # Initialize the sum to the first value
    sumval = data[0]
    # Remove the first value from the data
    data = data[1:]
    # Loop over the data
    for val in data:
        # Add the current value to the sum
        sumval += val

    # Return the sum
    return sumval