from gamegrid import Actor

class Auto(Actor):
    c_maxGeschw = 200
    c_ZeitBisMaxBeschleunigung = 4
    c_ZeitBisMaxStillstand = 300
    c_ZeitBisStillstandBremsen = 1

    def setGeschwindigkeit(self, geschw):
        self.v_geschwindigkeit = geschw

    def getGeschwindigkeit(self):
        return (self.v_geschwindigkeit)
    
    def Bremsen(self):
        if (self.v_geschwindigkeit > 0):
            self.v_geschwindigkeit = self.v_geschwindigkeit - (Auto.c_maxGeschw / Auto.c_ZeitBisStillstandBremsen/100)
        else:
            self.v_geschwindigkeit = 0

    def Beschleunigen(self):  
        autoGeschw = self.getGeschwindigkeit()
        
        if (self.v_geschwindigkeit < Auto.c_maxGeschw):
            
            autoGeschw = autoGeschw + (Auto.c_maxGeschw / Auto.c_ZeitBisMaxBeschleunigung / 10)
            self.setGeschwindigkeit(autoGeschw)
    
    def VerzoegerungDurchReibung(self):
        if (self.v_geschwindigkeit > 0):
            self.v_geschwindigkeit = self.v_geschwindigkeit - (Auto.c_maxGeschw / Auto.c_ZeitBisMaxStillstand)
        else:
            self.v_geschwindigkeit = 0         
               
    def Bewegen(self):
        if self.v_geschwindigkeit > 0:
            bewegung = int(self.v_geschwindigkeit/100)
            #print ("Bewegung: {}".format(bewegung)) 
            self.move(bewegung)
            
    def act(self):
        self.VerzoegerungDurchReibung()
        self.Bewegen()
        #print ("Geschwindigkeit: {}".format(self.v_geschwindigkeit)) 