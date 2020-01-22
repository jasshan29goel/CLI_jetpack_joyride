import time
import os
import random
import signal   
import sys

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

from colorama import init,Fore,Back
init()

class Board:

    def __init__(self):

        self._width = int(os.popen('stty size', 'r').read().split()[1])
        self._height = 30
        self._grid = np.array([[ [' ',None] for i in range(self._width+1)]
                     for j in range(self._height+1)])
        self._add=np.array([[0,0]])
        self._delete=np.array([[0,0]])
        self._bullets=[]
        self._snowBalls=[]
        self._beamsVertical=[]
        self._beamsHorizontal=[]
        self._beamsDiagnol=[]
        self._coins=[]
        self._magnets=[]
        self._timeLeft=140
        self._speed=[0.1,0,0]
        self._en=None
        self._charac=None

    def createBox(self):
        s="#"*self._width
        print("\033[91m","\033[1;1H",end='')
        print(s,end='')
        print("\033[30;1H",end='')
        print(s,end='')
        print("\033[91m","\033[30;1H")

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
        if ele1.name()=='character' and ele2.name()=='beam' and ele1.shield()==0:
            self.removeObject(ele1)
            ele1.lives=-1
            ele1.restore()
            if(ele1.lives<=0):
                self.quitX()
        if ele1.name()=='beam' and ele2.name()=='character' and ele2.shield()==0:
            self.removeObject(ele2)
            ele2.lives=-1
            ele2.restore()
            if(ele2.lives<=0):
                self.quitX()
        if ele1.name()=='character' and ele2.name()=='coin':
            self.removeObject(ele2)
            ele2.vanish()
            ele1.score=10
        if ele1.name()=='coin' and ele2.name()=='character':
            self.removeObject(ele1)
            ele1.vanish()
            ele2.score=10
        if ele1.name()=='bullet' and ele2.name()=='beam':
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()
        if ele1.name()=='beam' and ele2.name()=='bullet':
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()
        if ele1.name()=='bullet' and ele2.name()=='enemy':
            self.removeObject(ele1)
            if (ele1.position00()-10 == ele2.position00() or ele1.position00()-11 == ele2.position00()) and ele2.defense==0:
                ele2.lives=-1
                ele2.defense=0
                if ele2.lives<=0 :
                    self.quitX()
            ele1.vanish()
        if ele1.name()=='enemy' and ele2.name()=='bullet':
            self.removeObject(ele2)
            if (ele2.position00()-10 == ele1.position00() or ele2.position00()-11 == ele1.position00())and ele1.defense==0:
                ele1.lives=-1
                ele1.defense=0
                if ele1.lives<=0 :
                    self.quitX()
            ele2.vanish()
        if ele1.name()=='character' and ele2.name()=='snowBall'  and ele1.shield()==0:
            self.removeObject(ele2)
            ele2.vanish()
            self.removeObject(ele1)
            ele1.lives=-1
            ele1.restore()
            if(ele1.lives<=0):
                self.quitX()
        if ele1.name()=='snowBall' and ele2.name()=='character' and ele2.shield()==0:
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.lives=-1
            ele2.restore()
            if(ele2.lives<=0):
                self.quitX()
        if ele1.name()=='bullet' and ele2.name()=='snowBall' :
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()            
        if ele1.name()=='snowBall' and ele2.name()=='bullet' :
            self.removeObject(ele1)
            ele1.vanish()
            self.removeObject(ele2)
            ele2.vanish()
        if ele1.name()=='character' and ele2.name()=='enemy':
            self.quitX()
        if ele1.name()=='enemy' and ele2.name()=='character':
            self.quitX()

        return

    def quitX(self):
        if self._en.lives==0:
            print(Fore.WHITE,"You win Congrats")
            print(Fore.WHITE,"lives remaining: ",self._charac.lives)
            print(Fore.WHITE,"time remaining: ",self._timeLeft)
            print(Fore.WHITE,"score: ",self._charac.score+self._timeLeft*2 + 10*self._charac.lives)

        else:
            print(Fore.WHITE,"You lost")
            print(Fore.WHITE,"Boss lives left: ",self._en.lives)
        quit()

    def detectKey(self,character):
        char = self.user_input(self._speed[0])

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
            temp_bullet=bullet(character.position50(),character.position51())
            self._bullets.append(temp_bullet)
            self.writeObject(temp_bullet,character)
            character.score=-1
        if char == ' ' and time.time()-character.lastTime() > 70:
            character.activateShield(time.time())
        if char == 'p' and self._speed[2]==0:
            self._speed=[0.025,time.time(),1]
            
        self.write()
        if char == 'q':
            self.quitX()
	
    def writeObject(self,ele,character):
        for i in ele.position():
            if i[0] >=1 and i[1] >=1 and i[0]<=self._height and i[1]<=self._width: 
                if self._grid[i[0]][i[1]][0]!=' ':
                    self.collisionDetect(ele,self._grid[i[0]][i[1]][1])
                    break
                
        j=0
        ele_symbol=ele.symbol()
        for i in ele.position():
            if i[0] >=1 and i[1] >=1 and i[0]<=self._height and i[1]<=self._width: 
                self._grid[i[0]][i[1]]=[ele_symbol[j],ele]
                self._add=np.append(self._add,[i],axis=0)
            j=j+1
        return

    def removeObject(self,ele):
        for i in ele.position():
            if i[0] >=1 and i[1] >=1 and i[0]<=self._height and i[1]<=self._width: 
                self._grid[i[0]][i[1]]=[' ',None]
                self._delete=np.append(self._delete,[i],axis=0)
        return

   
    def write(self):
        for i in self._add[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self._height and i[1]<=self._width: 
                print(self.color(self._grid[i[0]][i[1]]),"\033["+str(i[0])+";"+str(i[1])+"H"+self._grid[i[0]][i[1]][0],end='')
        for i in self._delete[1:,:]:
            if i[0] >=1 and i[1] >=1 and i[0]<=self._height and i[1]<=self._width: 
                print(self.color(self._grid[i[0]][i[1]]),"\033["+str(i[0])+";"+str(i[1])+"H"+self._grid[i[0]][i[1]][0],end='')
        print(Fore.WHITE,"\033[30;1H")
        self._add=np.array([[0,0]])
        self._delete=np.array([[0,0]])
        return

    def color(self,ele):
        switcher = {
            "character":Fore.WHITE,
            "enemy":self.color_enemy(ele[0]),
            "beam":Fore.BLUE,
            "magnet":Fore.RED,
            "snowBall":Fore.WHITE,
            "bullet":Fore.LIGHTCYAN_EX,
            "coin":Fore.YELLOW,
        }
        if ele[1] is not None:
            return switcher.get(ele[1].name(),"")
        else:
            return ""
    def color_enemy(self,sym):
        if sym=='0':
            return Fore.BLACK
        elif sym!=' ':
            return Fore.WHITE
    def render(self):

        os.system('clear')
        self.createBox()

        # setup initial state
        character=boy(self._width,self._height,time.time())
        self._charac=character
        self.writeObject(character,character)
        enemy=boss(4,900)
        self._en=enemy
        self.writeObject(enemy,character)
        
        for i in range(5):
            self._beamsVertical.append(beamVertical(random.randint(2,25),random.randint(30,230)))
            self._beamsVertical.append(beamVertical(random.randint(2,25),random.randint(230,430)))
            self._beamsVertical.append(beamVertical(random.randint(2,25),random.randint(430,630)))
            self._beamsVertical.append(beamVertical(random.randint(2,25),random.randint(630,830)))
            self._beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(30,230)))
            self._beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(230,430)))
            self._beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(430,630)))
            self._beamsHorizontal.append(beamHorizontal(random.randint(2,29),random.randint(630,830)))
            self._beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(30,230)))
            self._beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(230,430)))
            self._beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(430,630)))
            self._beamsDiagnol.append(beamDiagnol(random.randint(2,25),random.randint(630,830)))
            self._coins.append(coin(random.randint(2,28),random.randint(30,330)))
            self._coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self._coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self._coins.append(coin(random.randint(2,28),random.randint(330,530)))
            self._coins.append(coin(random.randint(2,28),random.randint(530,830)))
            self._magnets.append(magnet(random.randint(2,29),random.randint(30,430)))                      
            self._magnets.append(magnet(random.randint(2,29),random.randint(430,830)))          


        # wirte initial state
        for i in self._beamsVertical:
            self.writeObject(i,character)
        for i in self._beamsHorizontal:
            self.writeObject(i,character)
        for i in self._beamsDiagnol:
            self.writeObject(i,character)
        for i in self._coins:
            self.writeObject(i,character)
        for i in self._magnets:
            self.writeObject(i,character)

        x=time.time()
        y=x
        enemy_time=x
        distToMagnet=[self._width+ self._height,-1,-1]
        while True:

            if time.time()-x > self._speed[0]:
                # update beams , coins , bullets
                for i in self._beamsVertical:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self._beamsHorizontal:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self._beamsDiagnol:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self._coins:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self._bullets:
                    self.removeObject(i)
                    i.write()
                    self.writeObject(i,character)
                for i in self._snowBalls:
                    self.removeObject(i)
                    i.write(enemy.lives)
                    self.writeObject(i,character)
                for i in self._magnets:
                    self.removeObject(i)
                    i.write()
                    if abs(i.position20()-character.position40())+abs(i.position21()-character.position41()) < distToMagnet[0]:
                        distToMagnet[0]=abs(i.position20()-character.position40())+abs(i.position21()-character.position41())
                        distToMagnet[1]=i.position20()
                        distToMagnet[2]=i.position21()
                    self.writeObject(i,character)
                # update characeter
                if distToMagnet[0]>15:
                    self.removeObject(character)
                    character.down()
                    self.writeObject(character,character)
                else:
                    self.removeObject(character)
                    character.towardsMagnet(distToMagnet[1],distToMagnet[2])
                    distToMagnet=[self._width+ self._height,-1,-1]
                    self.writeObject(character,character)

                

                x=time.time()
                if enemy.position01()>self._width-20:
                    self.removeObject(enemy)
                    enemy.write_right()
                    self.writeObject(enemy,character)
                    enemy.defense=1
                elif  x - enemy_time > 0.5:
                    if enemy.defense>0:
                        enemy.defense-=1
                    enemy_time=x
                    self.removeObject(enemy)
                    enemy.write_up_down(character.position30())
                    if character.position30() >= enemy.position00()+6 and character.position30() <= enemy.position00()+15:
                        self._snowBalls.append(snowBall(character.position30(),enemy.position01()-30))
                    elif character.position30() > enemy.position00()+15:
                        self._snowBalls.append(snowBall(enemy.position00()+12,enemy.position01()-30))
                    elif character.position30() < enemy.position00()+6:
                        self._snowBalls.append(snowBall(enemy.position00()+7,enemy.position01()-30))
                    self.writeObject(enemy,character)

                if x-character.lastTime() > 10 and x- character.liveLost() > 3:
                    character.deactivateShield()
                if self._speed[2]==1 and x-self._speed[1] > 10:
                    self._speed[0]=0.1
                self._timeLeft=int(140-(x-y))
                if 140-(x-y) < 0:
                    self.quitX()

                print(Fore.WHITE,"\033[2;2HLive:"+str(character.lives)+"  ",end='')
                print("\033[30;1H")
                print(Fore.WHITE,"\033[2;10HScore:"+str(character.score)+"  ",end='')
                print("\033[30;1H")
                print(Fore.WHITE,"\033[2;20HShield:"+str(int(x-character.lastTime()))+"  ",end='')
                print("\033[30;1H")
                print(Fore.WHITE,"\033[2;32HBoss:"+str(enemy.lives)+"  ",end='')
                print("\033[30;1H")
                print(Fore.WHITE,"\033[2;42HTime Remaining:"+str(int(140-(x-y)))+"  ",end='')
                print("\033[30;1H")

                self.write()
            self.detectKey(character)    
        return True

# os.system('mpg123 ./music/temp.mp3& ')

board=Board()
board.render()


