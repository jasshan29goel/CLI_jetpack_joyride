import time
import os
import random
import signal   

from getChUnix import _getChUnix as getChar
from alarmexception import AlarmException




class beamVertical:
    def __init__(self,n,m,width):
        self.position = [[n,m],[n+1,m],[n+2,m],[n+3,m],[n+4,m]] 
        self.tick=0
        self.width=width
    def writeBeamVertical(self):
        for i in self.position:
            if i[1]-self.tick >=1 and i[1]-self.tick <= self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick)+"H|",end='')
        print("\033[30;1H")
        self.tick=self.tick+1
        return        
    def removeBeamVertical(self):
        for i in self.position:
            if i[1]-self.tick+1 >=1 and i[1]-self.tick+1 <=self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick+1)+"H ",end='')
        print("\033[30;1H")
        return

class beamHorizontal:
    def __init__(self,n,m,width):
        self.position = [[n,m],[n,m+1],[n,m+2],[n,m+3],[n,m+4]] 
        self.tick=0
        self.width=width
    def writeBeamHorizontal(self):
        for i in self.position:
            if i[1]-self.tick >=1 and i[1]-self.tick <= self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick)+"H-",end='')
        print("\033[30;1H")
        self.tick=self.tick+1
        return        
    def removeBeamHorizontal(self):
        for i in self.position:
            if i[1]-self.tick+1 >=1 and i[1]-self.tick+1 <=self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick+1)+"H ",end='')
        print("\033[30;1H")
        return

class beamDiagnol:
    def __init__(self,n,m,width):
        self.position = [[n,m],[n+1,m+1],[n+2,m+2],[n+3,m+3],[n+4,m+4]] 
        self.tick=0
        self.width=width
    def writeBeamDiagnol(self):
        for i in self.position:
            if i[1]-self.tick >=1 and i[1]-self.tick <= self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick)+"H\\",end='')
        print("\033[30;1H")
        self.tick=self.tick+1
        return        
    def removeBeamDiagnol(self):
        for i in self.position:
            if i[1]-self.tick+1 >=1 and i[1]-self.tick+1 <=self.width:
                print("\033["+str(i[0])+";"+str(i[1]-self.tick+1)+"H ",end='')
        print("\033[30;1H")
        return
    
class Board:

    def __init__(self):

        self.width = int(os.popen('stty size', 'r').read().split()[1])
        self.height = 30
        self.grid = [[' ' for i in range(self.width)]
                     for j in range(self.height)]


    def createBox(self):
        s="#"*self.width
        print("\033[1;1H",end='')
        print(s,end='')
        print("\033[30;1H",end='')
        print(s,end='')
        print("\033[30;1H")

    def alarmhandler(self,signum, frame):
        raise AlarmException

    def user_input(self,timeout=1):
        signal.signal(signal.SIGALRM, self.alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
		
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    def detectKey(self):
        char = self.user_input()

        if char == 'd':
            print("d pressed")

        if char == 'a':
            print("a pressed")
        if char == 'q':
            quit()
	




    def render(self):

        os.system('clear')
        self.createBox()
        beamVertical1=beamVertical(8,50,self.width)
        beamVertical2=beamVertical(20,110,self.width)
        beamHorizontal1=beamHorizontal(14,30,self.width)
        beamHorizontal2=beamHorizontal(25,120,self.width)
        beamDiagnol1=beamDiagnol(3,140,self.width)
        beamDiagnol2=beamDiagnol(19,60,self.width)

        beamVertical1.writeBeamVertical()
        beamVertical2.writeBeamVertical()
        beamHorizontal1.writeBeamHorizontal()
        beamHorizontal2.writeBeamHorizontal()
        beamDiagnol1.writeBeamDiagnol()
        beamDiagnol2.writeBeamDiagnol()

        x=time.time()

        while True:
            if time.time()-x > 1:
                beamVertical1.removeBeamVertical()
                beamVertical2.removeBeamVertical()
                beamHorizontal1.removeBeamHorizontal()
                beamHorizontal2.removeBeamHorizontal()
                beamDiagnol1.removeBeamDiagnol()
                beamDiagnol2.removeBeamDiagnol()
                beamVertical1.writeBeamVertical()
                beamVertical2.writeBeamVertical()
                beamHorizontal1.writeBeamHorizontal()
                beamHorizontal2.writeBeamHorizontal()
                beamDiagnol1.writeBeamDiagnol()
                beamDiagnol2.writeBeamDiagnol()
                x=time.time()
            self.detectKey()    
        return True

board=Board()
board.render()


