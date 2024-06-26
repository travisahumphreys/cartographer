import csv
# Access a list like you would any array
#      li[0]   # => 1
# Look at the last element
#      li[-1]  # => 3
# Use [[] for _ in range(n)] to create n distinct lists.
def survey(source_map):
    file_path=source_map
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        first_row = next(reader)
        read_row = next(reader)
        map_buffer = [[]for _ in range(len(first_row)) ]
        measurements_in_inches = []
        callouts = []
        for callout in read_row:
            callouts.append(callout)
        for measurement in first_row:
            # Split the measurement on the "'" character
            feet, inches = measurement.split("' ")
            # Remove the double quote from the inches
            inches = inches.replace("''", '')
            # Convert the feet and inches to inches
            total_inches = int(feet) * 12 + float(inches)
            # Append the total inches to the list
            measurements_in_inches.append(total_inches)
        return measurements_in_inches
