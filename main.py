import svgwrite
import csv

 # 'in'  -  inch  -  “1in” equals “90px” (and therefore 90 user units)

# Create an instance of Drawing class
dwg = svgwrite.Drawing('test.svg', profile='full')
radius = input("Enter the radius of the circle: ")
# Set the size using the inch method from the created instance
dwg.attribs['height'] = '12in'
# Add a circle to the drawing
dwg.add(dwg.circle(center=('6in', '6in'), r=radius + "in", stroke='white', fill='red'))

# Save the drawing
dwg.save()