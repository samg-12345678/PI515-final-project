#https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random
from graphics import *

colorList=["Sienna","Old Lace","pink","Light Green"]
orderScoopCount=3
scoopCount=0
scoopYDistance=200
boxCount=len(colorList)
shopName="Ice Cream Shop"
# shopName=input("What would you like to call your Ice Cream Shop?" )

win = GraphWin(shopName,400,400)
win.setBackground("Light Blue")

def drawBoxes(color,boxX):
  box=Polygon(Point(30+boxX,300),Point(80+boxX,300),Point(80+boxX,400),Point(30+boxX,400))
  box.setFill(color)
  box.draw(win)

# def drawTrash():
#   trash=Rectangle(Point(360,200), Point(390,220))
#   trash.setFill("gray")
#   trash.draw(win)

def drawScoop(flavor,scoopX,scoopY):
  global c
  c=Circle(Point(scoopX,scoopY),15)
  c.setFill(flavor)
  c.draw(win)


def drawCone(coneX,coneY):
  cone=Polygon(Point(40+coneX,60+coneY),Point(60+coneX,60+coneY),Point(50+coneX,100+coneY))
  cone.setFill("Navajo White")
  cone.setOutline("Peru")
  cone.draw(win)

def drawTimer():
  timerText=Text(Point(300,50), "Timer:")
  timerText.draw(win)

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def updateScreen():
  # drawTrash()
  global orderScoopYDistance
  orderScoopYDistance=200
  global boxXDistance
  boxXDistance=0
  clear(win)
  drawTimer()
  drawCone(0,150) 
  for scoop in range(0,orderScoopCount) :
    orderScoopColor=colorList[random.randrange(0,len(colorList)-1)]
    drawScoop(orderScoopColor,50,orderScoopYDistance)
    orderScoopYDistance-=20
  for box in range(0,boxCount):
    drawBoxes(colorList[box],boxXDistance)
    boxXDistance+=50
  drawCone(260,150)
  
updateScreen()

while True:
  for scoop in range(0,orderScoopCount) :
  # to limit the number of scoops use a while loop | example: while scoopCount<orderScoopCount :
    clickPoint = win.getMouse()
    if clickPoint.getY()>300 and clickPoint.getX()<230 and clickPoint.getX()>30:
      if clickPoint.getX()<80 :
        scoopColor=colorList[0]
      elif clickPoint.getX()<130 :
        scoopColor=colorList[1]
      elif clickPoint.getX()<180 :
        scoopColor=colorList[2]
      elif clickPoint.getX()<230 :
        scoopColor=colorList[3]
      # elif clickPoint.getX()<280 :
      #   scoopColor=colorList[4]
      # elif clickPoint.getX()<330 :
      #   scoopColor=colorList[5]
      drawScoop(scoopColor,310,scoopYDistance)
      scoopYDistance-=20
      scoopCount+=1

    # elif clickPoint.getX()>360 and clickPoint.getX()<390 and clickPoint.getY()>200 and clickPoint.getY()<220 and scoopCount>orderScoopCount:
    #     c.undraw()
    #     scoopCount-=1
    #     if scoopYDistance<200:
    #      scoopYDistance+=20
    if scoopCount==6: # replace with conditional that checks if "serve" button was clicked
      updateScreen()
      scoopYDistance=200
      scoopCount=0
