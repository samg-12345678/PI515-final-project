#https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random
colorList=["red","orange","yellow","pink","white"]
color=colorList[random.randrange(0,len(colorList)-1)]
from graphics import *
def main():
  win = GraphWin("My Circle",400,400)
  c=Circle(Point(50,30),10)
  c.setFill(color)
  c.draw(win)
  c=Circle(Point(50,50),10)
  c.setFill("pink")
  c.draw(win)
  aPolygon=Polygon(Point(40,60),Point(60,60),Point(50,100))
  aPolygon.setFill("brown")
  aPolygon.draw(win)
  win.getMouse()
  win.close()

main()
  