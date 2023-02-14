#https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random
from graphics import *

colorList=["Sienna","Old Lace"]
addColorList=["pink","Light Green","red","orange"]
orderScoopCount=4
scoopCount=0
scoopYDistance=200
boxXDistance2=80
boxCount=len(colorList)
shopBoxXDistance=80
orderCount=0
shopName="Ice Cream Shop"
# shopName=input("What would you like to call your Ice Cream Shop?" )

win = GraphWin(shopName,400,400)
win.setBackground("Light Blue")

def drawBoxes(color,boxX,winName):
  box=Rectangle(Point(30+boxX,300),Point(80+boxX,400))
  box.setFill(color)
  box.draw(winName)

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
  boxCount=len(colorList)
  clear(win)
  drawTimer()
  drawCone(0,150) 
  for scoop in range(0,orderScoopCount) :
    orderScoopColor=colorList[random.randrange(0,len(colorList))]
    drawScoop(orderScoopColor,50,orderScoopYDistance)
    orderScoopYDistance-=20
  for box in range(0,boxCount):
    drawBoxes(colorList[box],boxXDistance,win)
    boxXDistance+=50
  drawCone(260,150)
  

while True:
  updateScreen()
  for scoop in range(0,orderScoopCount) :
  # to limit the number of scoops use a while loop | example: while scoopCount<orderScoopCount :
    boxCount=len(colorList)
    clickPoint = win.getMouse()
    if clickPoint.getY()>300 and clickPoint.getX()<(20+boxCount*50) and clickPoint.getX()>30:
      for box in range(0,boxCount):
        if clickPoint.getX()<boxXDistance2:
          scoopColor=colorList[box]
          break
        else:
          boxXDistance2+=50
      drawScoop(scoopColor,310,scoopYDistance)
      scoopYDistance-=20
      scoopCount+=1
      boxXDistance2=80
# vvv trash button wip
    # elif clickPoint.getX()>360 and clickPoint.getX()<390 and clickPoint.getY()>200 and clickPoint.getY()<220 and scoopCount>orderScoopCount:
    #     c.undraw()
    #     scoopCount-=1
    #     if scoopYDistance<200:
    #      scoopYDistance+=20
    if scoopCount==orderScoopCount: # replace with conditional that checks if "serve" button was clicked ?
      updateScreen()
      scoopYDistance=200
      scoopCount=0
      orderCount+=1
    if orderCount == 3: # number of orders to visit shop
      shopWin = GraphWin("Upgrades Shop",400,400)
      boxXDistance=0 
      for box in range(0,len(addColorList)):
        drawBoxes(addColorList[box],boxXDistance,shopWin)
        boxXDistance+=50
      timerText=Text(Point(200,50), "Welcome to the Upgrades Shop!")
      timerText.draw(shopWin)
      shopClickPoint = shopWin.getMouse()
      if shopClickPoint.getY()>300 and shopClickPoint.getX()<(20+(len(addColorList)*50)) and shopClickPoint.getX()>30:
        for box in range(0,len(addColorList)):
          if shopClickPoint.getX()<shopBoxXDistance:
            colorList.append(addColorList[box])
            addColorList.remove(addColorList[box])
            break
          else:
            shopBoxXDistance+=50
        shopBoxXDistance=80
      shopWin.close()
      orderCount=0