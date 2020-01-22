import numpy as np
import time
class boy:
    def __init__(self,width,height,time):
        self._position = np.array([[27,3],[27,4],[27,5],[28,3],[28,4],[28,5],[29,3],[29,4],[29,5]])
        self._symbol = np.array([' ','O',' ','[','|','\\',' ','/','|'])
        self._width=width
        self._height=height
        self._name='character'
        self._lives=5
        self._score=0
        self._shield=0
        self._lastTime=time-70
        self._liveLost=-1
        self._gravity_speed=1
    def up(self):
        if self._position[0][0]>=4:
            self._position[:,0]=self._position[:,0]-2
            self._gravity_speed=1
    def left(self):
        if self._position[0][1]>=3:
            self._position[:,1]=self._position[:,1]-2
    def right(self):
        if self._position[0][1]<=self._width-4:
            self._position[:,1]=self._position[:,1]+2
    def down(self):
        if self._position[0][0]<=self._height-3-int(self._gravity_speed):
            self._position[:,0]=self._position[:,0]+int(self._gravity_speed)
            self._gravity_speed+=0.3
        else:
            self._position[:,0]=self._position[:,0]+self._height-3-self._position[0][0]
    def towardsMagnet(self,n,m):
        if self._position[4][0]-n > 0 and self._position[0][0]>=4:
            self._position[:,0]=self._position[:,0]-2
        elif self._position[4][0]-n < 0 and self._position[0][0]<=self._height-5:
            self._position[:,0]=self._position[:,0]+2
        if self._position[4][1]-m > 0 and self._position[0][1]>=3:
            self._position[:,1]=self._position[:,1]-2
        elif self._position[4][1]-m < 0 and self._position[0][1]<=self._width-4:
            self._position[:,1]=self._position[:,1]+2
        return 
    def restore(self):
        self._position = np.array([[27,3],[27,4],[27,5],[28,3],[28,4],[28,5],[29,3],[29,4],[29,5]])
        self._liveLost=time.time()
        self._symbol = np.array(['O','/','|','|','\\','|','/','|','|'])
        self._shield=1
    def activateShield(self,time):
        self._symbol = np.array(['O','/','|','|','\\','|','/','|','|'])
        self._shield=1
        self._lastTime=time
    def deactivateShield(self):
        self._symbol = np.array([' ','O',' ','[','|','\\',' ','/','|'])
        self._shield=0
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name
    def shield(self):
        return self._shield
    def liveLost(self):
        return self._liveLost
    def lastTime(self):
        return self._lastTime
    def score(self):
        return self._score
    def setscore(self,k):
        self._score+=k
    def lives(self):
        return self._lives
    def setlives(self,k):
        self._lives+=k
    def position30(self):
        return self._position[3][0]
    def position50(self):
        return self._position[5][0]
    def position51(self):
        return self._position[5][1]
    def position40(self):
        return self._position[4][0]
    def position41(self):
        return self._position[4][1]
    lives = property(lives, setlives)
    score = property(score, setscore)