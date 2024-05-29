
# cartographer

don't forget to `sudo apt-get upgrade` every once in a while

# CSV Syntax
The first row of the CSV file acts as a blueprint for the x-axis positions of components in your wiring diagram. Each column corresponds to a specific x-coordinate, calculated based on the measurement converted to inches. The subsequent rows define the types of components or wire paths at different y-coordinate increments (0.5 inches per row).



## Simplified Example

<div style="display: flex; justify-content: center;">
  <pre style="text-align: left;">2' 0'',1' 6'',1' 0'',0' 6'',0' 0''
  C   ,   -  ,   B  ,   B  ,  C
      ,      ,   |  ,   |  ,
      ,   C  ,   ┘  ,   └  ,  C</pre>
</div>

<div style="display: grid; justify-content: center;">
  <pre style="text-align: left;">2' 0'',1' 6'',1' 0'',0' 6'',0' 0''
C,-,B,B,C
,,|,|,
,C,┘,└,C</pre>
</div>
</html>