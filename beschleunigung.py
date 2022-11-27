from gamegrid import *
from auto import Auto
'class meinauto(Auto):
def Steuern(tastencode):
    if tastencode == 38:
        meinauto.Beschleunigen()        
    
    if tastencode == 40:
        meinauto.Bremsen()
        
    if tastencode == 39:
        meinauto.turn(5) 
         
    if tastencode == 37:
        meinauto.turn(-5)  
        
feld = GameGrid(900,500)
meinauto = Auto(True,"sprites/arrow1.png")
hintergrund = Actor("sprites/racetrack.gif")

meinauto.setGeschwindigkeit(0)
feld.setBgColor(255,255,255)
feld.setSimulationPeriod(10)

feld.addActor(hintergrund,Location(300,250))
feld.addActor(meinauto,Location(300,300))
feld.addKeyRepeatListener(Steuern)

feld.show() 
feld.doRun()
#print ("Zahl {} {}".format(1,2))