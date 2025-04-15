import numpy as np

def create_series_and_sum(first, last, step):
    # Create the series
    series = np.arange(first, last , step, dtype=float)  # Include last element in the series

    # Print the series
    print("Series:", series)

    # Calculate and print the sum of the series
    series_sum = np.sum(series)
    print("Sum of series:", series_sum)

# Input from the user
first_member = float(input("Enter the first member of the series: "))
last_member = float(input("Enter the last member of the series: "))
interval_size = float(input("Enter the interval size: "))

# Generate and print series and its sum
create_series_and_sum(first_member, last_member, interval_size)
