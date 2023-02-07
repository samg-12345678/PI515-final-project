#https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
from graphics import *
def drawIceCream():
  win = GraphWin("My Circle",400,400)
  c=Circle(Point(50,30),10)
  c.setFill("white")
  c.draw(win)
  c=Circle(Point(50,50),10)
  c.setFill("pink")
  c.draw(win)
  cone=Polygon(Point(40,60),Point(60,60),Point(50,100))
  cone.setFill("brown")
  cone.draw(win)
  win.getMouse()
  win.close()

drawIceCream()

  