<style>.wrapper {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 10px;
  grid-auto-rows: 100px;
  grid-template-areas:
    "a a a b b c c c"
    "a a a b b c c c"
    "a a a b b c c c"
    "a a a b b c c c";
  align-items: start;
}
.item1 {
  grid-area: a;
}
.item2 {
  grid-area: b;
}
.item3 {
  grid-area: c;
}
</style>
# cartographer

don't forget to `sudo apt-get upgrade` every once in a while

# CSV Syntax
The first row of the CSV file acts as a blueprint for the x-axis positions of components in your wiring diagram. Each column corresponds to a specific x-coordinate, calculated based on the measurement converted to inches. The subsequent rows define the types of components or wire paths at different y-coordinate increments (0.5 inches per row).
<div class="wrapper">
  <div class="item2"><pre>2' 0'',1' 6'',1' 0'',0' 6'',0' 0''
  C   ,   -  ,   B  ,   B  ,  C
      ,      ,   |  ,   |  ,
      ,   C  ,   ┘  ,   └  ,  C</pre>
  </div>
</div>