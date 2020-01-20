import time
import os
import random
import signal   
import numpy as np


from beam import beamDiagnol,beamHorizontal,beamVertical
from boy import boy
from coin import coin
from bullet import bullet
from snowBall import snowBall
from boss import boss
from magnet import magnet

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
        self.snowBalls=[]
        self.beamsVertical=[]
        self.beamsHorizontal=[]
        self.beamsDiagnol=[]
        self.coins=[]
        self.magnets=[]
        self.timeLeft=140
        self.speed=[0.1,0,0]
        self.en=None
        self.charac=None

    def createBox(self):
        s="#"*self.width
        print("\033[1;1H",end='')
        print(s,end='')
        print("\033[30;1H",end='')
        print(s,end='')
        print("\033[30;1H")

    def alarmhandler(self,signum, frame):
        raise AlarmException

    def user_input(self,timeout):
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
                self.quitX()
        if ele1.name=='beam' and ele2.name=='character' and ele2.shield==0:
            self.removeObject(ele2)
            ele2.lives-=1
            ele2.restore()
            if(ele2.lives<=0):
                self.quitX()
        if ele1.name=='character' and ele2.name=='coin':
            self.removeObject(ele2)
            ele2.vanish()
            ele1.score+=10
        if ele1.name=='coin' and ele2.name=='character':
            self.removeObject(ele1)
            ele1.vanish()
            ele2.score+=10
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
        if ele1.name=='bullet' and ele2.name=='enemy':
            self.removeObject(ele1)
            if (ele1.position[0][0]-10 == ele2.position[0][0] or ele1.position[0][0]-11 == ele2.position[0][0]) and ele2.defense==0:
                ele2.lives-=1
                ele2.defense=1
                if ele2.lives<=0 :
                    self.quitX()
            ele1.vanish()
        if ele1.name=='enemy' and ele2.name=='bullet':
            self.removeObject(ele2)
            if (ele2.position[0][0]-10 == ele1.position[0][0] or ele2.position[0][0]-11 == ele1.position[0][0])and ele1.defense==0:
                ele1.lives-=1
                ele1.defense=1
                if ele1.lives<=0 :
                    self.quitX()
            ele2.vanish()
        if ele1.name=='character' and ele2.name=='snowBall'  and ele1.shield==0:
            self.removeObject(ele2)
            ele2.vanish()
            self.removeObject(ele1)
            ele1.lives-=1
            ele1.restore()
            if(ele1.lives<=0):
                self.quitX()
        if ele1.name=='snowBall' and ele2.name=='character' and ele2.shield==0:
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.lives-=1
            ele2.restore()
            if(ele2.lives<=0):
                self.quitX()
        if ele1.name=='bullet' and ele2.name=='snowBall' :
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()            
        if ele1.name=='snowBall' and ele2.name=='bullet' :
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()
        if ele1.name=='character' and ele2.name=='enemy':
            self.quitX()
        if ele1.name=='enemy' and ele2.name=='character':
            self.quitX()

        return

    def quitX(self):
        if self.en.lives==0:
            print("You win Congrats")
            print("lives remaining: ",self.charac.lives)
            print("time remaining: ",self.timeLeft)
            print("score: ",self.charac.score+self.timeLeft*5 + 10*self.charac.lives)

        else:
            print("You lost")
            print("Boss lives left: ",self.en.lives)
        quit()

    def detectKey(self,character):
        char = self.user_input(self.speed[0])

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
            temp_bullet=bullet(character.position[5][0],character.position[5][1])
            self.bullets.append(temp_bullet)
            self.writeObject(temp_bullet,character)
            character.score-=1
        if char == ' ' and time.time()-character.lastTime > 70:
            character.activateShield(time.time())
        if char == 'p' and self.speed[2]==0:
            self.speed=[0.025,time.time(),1]
            
        self.write()
        if char == 'q':
            self.quitX()
	
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
        self.charac=character
        self.writeObject(character,character)
        enemy=boss(4,900)
        self.en=enemy
        self.writeObject(enemy,character)
        
        for i in range(5):
            self.beamsVertical.append(beamVertical(random.randint(2,25),random.randint(30,230)))
            self.beamsVertical.append(beamVertical(random.randint(2,25),random.randint(230,430)))
            self.beamsVertical.append(beamVertical(random.randint(2,25),random.randint(430,630)))
            self.beamsVertical.append(beamVertical(random.randint(2,25),random.randint(630,830)))
            self.beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(30,230)))
            self.beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(230,430)))
            self.beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(430,630)))
            self.beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(630,830)))
            self.beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(30,230)))
            self.beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(230,430)))
            self.beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(430,630)))
            self.beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(630,830)))
            self.coins.append(coin(random.randint(2,28),random.randint(30,330)))
            self.coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self.coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self.coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self.coins.append(coin(random.randint(2,28),random.randint(530,830)))
            self.magnets.append(magnet(random.randint(2,29),random.randint(30,430)))                      
            self.magnets.append(magnet(random.randint(2,29),random.randint(430,830)))          


        # wirte initial state
        for i in self.beamsVertical:
            self.writeObject(i,character)
        for i in self.beamsHorizontal:
            self.writeObject(i,character)
        for i in self.beamsDiagnol:
            self.writeObject(i,character)
        for i in self.coins:
            self.writeObject(i,character)
        for i in self.magnets:
            self.writeObject(i,character)


        x=time.time()
        y=x
        enemy_time=x
        distToMagnet=[self.width+ self.height,-1,-1]
        while True:

            if time.time()-x > self.speed[0]:
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
                    self.writeObject(i,character)
                for i in self.snowBalls:
                    self.removeObject(i)
                    i.write(enemy.lives)
                    self.writeObject(i,character)
                for i in self.magnets:
                    self.removeObject(i)
                    i.write()
                    if abs(i.position[2][0]-character.position[4][0])+abs(i.position[2][1]-character.position[4][1]) < distToMagnet[0]:
                        distToMagnet[0]=abs(i.position[2][0]-character.position[4][0])+abs(i.position[2][1]-character.position[4][1])
                        distToMagnet[1]=i.position[2][0]
                        distToMagnet[2]=i.position[2][1]
                    self.writeObject(i,character)
                # update characeter
                if distToMagnet[0]>10:
                    self.removeObject(character)
                    character.down()
                    self.writeObject(character,character)
                else:
                    self.removeObject(character)
                    character.towardsMagnet(distToMagnet[1],distToMagnet[2])
                    distToMagnet=[self.width+ self.height,-1,-1]
                    self.writeObject(character,character)

                

                x=time.time()
                if enemy.position[0][1]>self.width-20:
                    self.removeObject(enemy)
                    enemy.write_right()
                    self.writeObject(enemy,character)
                    enemy.defense=1
                elif  x - enemy_time > 0.5:
                    enemy.defense=0
                    enemy_time=x
                    self.removeObject(enemy)
                    enemy.write_up_down()
                    if character.position[3][0] >27:
                        self.snowBalls.append(snowBall(27,enemy.position[0][1]-30))
                    elif character.position[3][0]<3:
                        self.snowBalls.append(snowBall(3,enemy.position[0][1]-30))
                    else :
                        self.snowBalls.append(snowBall(character.position[3][0],enemy.position[0][1]-30))
                    self.writeObject(enemy,character)

                if x-character.lastTime > 10 and x- character.liveLost > 3:
                    character.deactivateShield()
                if self.speed[2]==1 and x-self.speed[1] > 10:
                    self.speed[0]=0.1
                self.timeLeft=int(140-(x-y))
                if 140-(x-y) < 0:
                    self.quitX()

                print("\033[2;2HLive:"+str(character.lives)+"  ",end='')
                print("\033[30;1H")
                print("\033[2;10HScore:"+str(character.score)+"  ",end='')
                print("\033[30;1H")
                print("\033[2;20HShield:"+str(int(x-character.lastTime))+"  ",end='')
                print("\033[30;1H")
                print("\033[2;32HBoss:"+str(enemy.lives)+"  ",end='')
                print("\033[30;1H")
                print("\033[2;42HTime Remaining:"+str(int(140-(x-y)))+"  ",end='')
                print("\033[30;1H")

                self.write()
            self.detectKey(character)    
        return True

board=Board()
board.render()


