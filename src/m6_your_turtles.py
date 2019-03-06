"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zixin Fan.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window=rg.TurtleWindow()
window.tracer(10)

c=rg.SimpleTurtle()
c.pen=rg.Pen('green yellow',10)

c.pen_up()
c.go_to(rg.Point(-25,200))
c.pen_down()

c.right(135)

for i in range(6):
    for k in range(360):
        c.left(1)
        c.forward(0.4)
    for j in range(15):
        c.left(1)
        c.forward(5)

c.left(135)

for i in range(4):
    for j in range(15):
        c.right(1)
        c.forward(5)
    for k in range(360):
        c.right(1)
        c.forward(0.3)


d=rg.SimpleTurtle()
d.pen=rg.Pen('blue',5)

d.left(30)

for k in range(2):
    for i in range(360):
        d.right(1)
        d.forward(0.3)
    d.right(120)

d.right(90)

for i in range(90):
    d.right(1)
    d.forward(0.3)

d.pen_up()
d.go_to(rg.Point(0,0))
d.pen_down()

d.left(90)

for i in range(90):
    d.left(1)
    d.forward(0.3)

window.close_on_mouse_click()