import time
import os
import random
import signal   
import numpy as np

from beam import beamDiagnol,beamHorizontal,beamVertical
from boy import boy
from getChUnix import _getChUnix as getChar
from alarmexception import AlarmException


class Board:

    def __init__(self):

        self.width = int(os.popen('stty size', 'r').read().split()[1])
        self.height = 30
        self.grid = np.array([[' ' for i in range(self.width+1)]
                     for j in range(self.height+1)])
        self.add=np.array([[0,0]])
        self.delete=np.array([[0,0]])


    def createBox(self):
        s="#"*self.width
        print("\033[1;1H",end='')
        print(s,end='')
        print("\033[30;1H",end='')
        print(s,end='')
        print("\033[30;1H")

    def alarmhandler(self,signum, frame):
        raise AlarmException

    def user_input(self,timeout=0.15):
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

    def collisionDetect(self,ele):
        j=0
        for i in ele.position:
            if self.grid[i[0]][i[1]] !=ele.symbol[j]:
                ele.lives=ele.lives-1
                time.sleep(1)
                if ele.lives <=0:
                    quit()
                return
            j=j+1

    def detectKey(self,character):
        char = self.user_input()

        if char == 'w':
            self.removeObject(character)
            character.up()
            self.writeObject(character,character)

        if char == 'a':
            self.removeObject(character)
            character.left()
            self.writeObject(character,character)

        if char == 'd':
            self.removeObject(character)
            character.right()
            self.writeObject(character,character)
        
        self.write()
        if char == 'q':
            quit()
	
    def writeObject(self,ele,character):
        j=0
        for i in ele.position:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                if self.grid[i[0]][i[1]]==' ': 
                    self.grid[i[0]][i[1]]=ele.symbol[j]
                else :
                    self.collisionDetect(character)
                self.add=np.append(self.add,[i],axis=0)
            j=j+1
        return

    def removeObject(self,ele):
        for i in ele.position:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                self.grid[i[0]][i[1]]=' '
                self.delete=np.append(self.delete,[i],axis=0)
        return

   
    def write(self):
        for i in self.add[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                print("\033["+str(i[0])+";"+str(i[1])+"H"+self.grid[i[0]][i[1]],end='')
        for i in self.delete[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                print("\033["+str(i[0])+";"+str(i[1])+"H"+self.grid[i[0]][i[1]],end='')
        print("\033[30;1H")
        self.add=np.array([[0,0]])
        self.delete=np.array([[0,0]])
        return


    def render(self):

        os.system('clear')
        self.createBox()
        character=boy(self.width,self.height)
        beamVertical1=beamVertical(2,100)
        beamVertical2=beamVertical(24,100)
        beamHorizontal1=beamHorizontal(10,120)
        beamHorizontal2=beamHorizontal(22,120)
        beamDiagnol1=beamDiagnol(10,150)
        beamDiagnol2=beamDiagnol(20,150)

        self.writeObject(character,character)
        self.writeObject(beamVertical1,character)
        self.writeObject(beamVertical2,character)
        self.writeObject(beamHorizontal1,character)
        self.writeObject(beamHorizontal2,character)
        self.writeObject(beamDiagnol1,character)
        self.writeObject(beamDiagnol2,character)
        self.write()


        x=time.time()

        while True:
            if time.time()-x > 0.15:
                self.removeObject(beamVertical1)
                self.removeObject(beamVertical2)
                self.removeObject(beamHorizontal1)
                self.removeObject(beamHorizontal2)
                self.removeObject(beamDiagnol1)
                self.removeObject(beamDiagnol2)
                beamVertical1.write()
                beamVertical2.write()
                beamHorizontal1.write()
                beamHorizontal2.write()
                beamDiagnol1.write()
                beamDiagnol2.write()
                self.writeObject(beamVertical1,character)
                self.writeObject(beamVertical2,character)
                self.writeObject(beamHorizontal1,character)
                self.writeObject(beamHorizontal2,character)
                self.writeObject(beamDiagnol1,character)
                self.writeObject(beamDiagnol2,character)
 
                self.removeObject(character)
                character.down()
                self.writeObject(character,character)

                print("\033[2;2H  "+str(character.lives)+"  ",end='')
                print("\033[30;1H")

                self.write()
                x=time.time()
            self.detectKey(character)    
        return True

board=Board()
board.render()


