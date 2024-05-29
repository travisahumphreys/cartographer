import csv
file_path =input("Enter the path to the CSV file: ")
# Open the CSV file.
def read_csv(file_path):
    with open(file_path, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        # Get the first row
        first_row = next(reader)
        # Create an empty list to store the measurements in inches
        measurements_in_inches = []
        # Iterate over the measurements in the first row
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

print(read_csv(file_path))