import svgwrite
import csv
import rework.surveyor as surveyor
 # 'in'  -  inch  -  “1in” equals “90px” (and therefore 90 user units)

# Create an instance of Drawing class
dwg = svgwrite.Drawing('./drawings/test.svg', profile='full')
file_path=input("Enter the path to the CSV file: ")
reader = surveyor.read_csv(file_path)
radius = input("Enter the radius of the circle: ")
# Set the size using the inch method from the created instance
dwg.attribs['height'] = '12in'
# Add a circle to the drawing
dwg.add(dwg.circle(center=('6in', '6in'), r=radius + "in", stroke='black'))
print(surveyor.read_csv(file_path))
# Save the drawing
#dwg.save()