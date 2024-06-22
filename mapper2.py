import csv
import json
source_map = "./map/5526.csv"


def survey(source_map):
    with open(source_map, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)
        map_buffer = {header: [row[i] for row in data] for i, header in enumerate(headers)}
        return map_buffer

print(json.dumps(survey(source_map), indent=4))
#        measurements_in_inches = []
##        callouts = []
##        for callout in read_row:
##            callouts.append(callout)
#        for measurement in read_row:
#            # Split the measurement on the "'" character
#            feet, inches = measurement.split("' ")
#            # Remove the double quote from the inches
#            inches = inches.replace("''", '')
#            # Convert the feet and inches to inches
#            total_inches = int(feet) * 12 + float(inches)
#            # Append the total inches to the list
#            measurements_in_inches.append(total_inches)
#        return measurements_in_inches
#