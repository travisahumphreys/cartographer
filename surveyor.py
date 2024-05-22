import csv

# Open the CSV file
# Open the CSV file
with open('./csv/asciimap.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    # Get the first row
    first_row = next(reader)

    measurements_in_inches = []                      # Create an empty list to store the measurements in inches  
    for measurement in first_row:                    # Iterate over the measurements in the first row
        feet, inches = measurement.split("' ")       # Split the measurement on the "'" character
        inches = inches.replace("''", '')            # Remove the double quote from the inches
        total_inches = int(feet) * 12 + float(inches)# Convert the feet and inches to inches
        measurements_in_inches.append(total_inches)  # Append the total inches to the list

  #  branch_counter = []
  #  for col in measurements_in_inches:
  #      branch_counter.append(branch)
print(measurements_in_inches)