import time
import os
import random
import signal   
import numpy as np

from beam import beamDiagnol,beamHorizontal,beamVertical
from boy import boy
from coin import coin
from bullet import bullet
from getChUnix import _getChUnix as getChar
from alarmexception import AlarmException


class Board:

    def __init__(self):

        self.width = int(os.popen('stty size', 'r').read().split()[1])
        self.height = 30
        self.grid = np.array([[ [' ',None] for i in range(self.width+1)]
                     for j in range(self.height+1)])
        self.add=np.array([[0,0]])
        self.delete=np.array([[0,0]])
        self.bullets=[]
        self.beamsVertical=[]
        self.beamsHorizontal=[]
        self.beamsDiagnol=[]
        self.coins=[]

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

    def collisionDetect(self,ele1,ele2):
        if ele1.name=='character' and ele2.name=='beam' and ele1.shield==0:
            self.removeObject(ele1)
            ele1.lives-=1
            ele1.restore()
            if(ele1.lives<=0):
                quit()
        if ele1.name=='beam' and ele2.name=='character' and ele2.shield==0:
            self.removeObject(ele2)
            ele2.lives-=1
            ele2.restore()
            if(ele2.lives<=0):
                quit()
        if ele1.name=='character' and ele2.name=='coin':
            self.removeObject(ele2)
            ele2.vanish()
            ele1.score+=2
        if ele1.name=='coin' and ele2.name=='character':
            self.removeObject(ele1)
            ele1.vanish()
            ele2.score+=2
        if ele1.name=='bullet' and ele2.name=='beam':
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()
        if ele1.name=='beam' and ele2.name=='bullet':
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()

        return


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

        if char == 'b':
            self.bullets.append(bullet(character.position[5][0],character.position[5][1]))
            character.score-=1
        if char == ' ' and time.time()-character.lastTime > 70:
            character.activateShield(time.time())
            
        self.write()
        if char == 'q':
            quit()
	
    def writeObject(self,ele,character):
        for i in ele.position:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                if self.grid[i[0]][i[1]][0]!=' ':
                    self.collisionDetect(ele,self.grid[i[0]][i[1]][1])
                    break
                
        j=0
        for i in ele.position:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                 
                self.grid[i[0]][i[1]]=[ele.symbol[j],ele]
                self.add=np.append(self.add,[i],axis=0)
            j=j+1
        return

    def removeObject(self,ele):
        for i in ele.position:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                self.grid[i[0]][i[1]]=[' ',None]
                self.delete=np.append(self.delete,[i],axis=0)
        return

   
    def write(self):
        for i in self.add[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                print("\033["+str(i[0])+";"+str(i[1])+"H"+self.grid[i[0]][i[1]][0],end='')
        for i in self.delete[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self.height and i[1]<=self.width: 
                print("\033["+str(i[0])+";"+str(i[1])+"H"+self.grid[i[0]][i[1]][0],end='')
        print("\033[30;1H")
        self.add=np.array([[0,0]])
        self.delete=np.array([[0,0]])
        return


    def render(self):

        os.system('clear')
        self.createBox()

        # setup initial state
        character=boy(self.width,self.height,time.time())
        self.beamsVertical.extend([
            beamVertical(2,100),
            beamVertical(21,100),
            beamVertical(4,240),
            beamVertical(11,240),
            beamVertical(18,240),
            beamVertical(7,250),
            beamVertical(15,250),
            beamVertical(22,250)
        ])
        self.beamsHorizontal.extend([
            beamHorizontal(10,120),
            beamHorizontal(22,120)
        ])
        self.beamsDiagnol.extend([
            beamDiagnol(10,150),
            beamDiagnol(20,150)
        ])
        self.coins.extend([
            coin(28,30),
            coin(25,190),
            coin(5,190)
        ])

        # wirte initial state
        for i in self.beamsVertical:
            self.writeObject(i,character)
        for i in self.beamsHorizontal:
            self.writeObject(i,character)
        for i in self.beamsDiagnol:
            self.writeObject(i,character)
        for i in self.coins:
            self.writeObject(i,character)


        x=time.time()

        while True:
            if time.time()-x > 0.15:
                # update beams , coins , bullets
                for i in self.beamsVertical:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self.beamsHorizontal:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self.beamsDiagnol:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self.coins:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self.bullets:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,bullet)

                # update characeter
                self.removeObject(character)
                character.down()
                self.writeObject(character,character)
                
                x=time.time()
                if x-character.lastTime > 10:
                    character.deactivateShield()

                print("\033[2;2HLive:"+str(character.lives)+"  ",end='')
                print("\033[30;1H")
                print("\033[2;10HScore:"+str(character.score)+"  ",end='')
                print("\033[30;1H")
                print("\033[2;20HTimeout:"+str(int(x-character.lastTime))+"  ",end='')
                print("\033[30;1H")

                self.write()
            self.detectKey(character)    
        return True

board=Board()
board.render()


