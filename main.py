import csv
import csv
# import svgutils

with open('./csv/test.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)