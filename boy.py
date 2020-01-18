import numpy as np
import time
class boy:
    def __init__(self,width,height,time):
        self.position = np.array([[27,3],[27,4],[27,5],[28,3],[28,4],[28,5],[29,3],[29,4],[29,5]])
        self.symbol = np.array([' ','O',' ','[','|','\\',' ','/','|'])
        self.width=width
        self.height=height
        self.name='character'
        self.lives=5
        self.score=0
        self.shield=0
        self.lastTime=time-70
        self.liveLost=-1
    def up(self):
        if self.position[0][0]>=4:
            self.position[:,0]=self.position[:,0]-2
    def left(self):
        if self.position[0][1]>=3:
            self.position[:,1]=self.position[:,1]-2
    def right(self):
        if self.position[0][1]<=self.width-4:
            self.position[:,1]=self.position[:,1]+2
    def down(self):
        if self.position[0][0]<=self.height-4:
            self.position[:,0]=self.position[:,0]+1
    def towardsMagnet(self,n,m):
        if self.position[4][0]-n > 0 and self.position[0][0]>=4:
            self.position[:,0]=self.position[:,0]-2
        elif self.position[4][0]-n < 0 and self.position[0][0]<=self.height-5:
            self.position[:,0]=self.position[:,0]+2
        if self.position[4][1]-m > 0 and self.position[0][1]>=3:
            self.position[:,1]=self.position[:,1]-2
        elif self.position[4][1]-m < 0 and self.position[0][1]<=self.width-4:
            self.position[:,1]=self.position[:,1]+2
        return 
    def restore(self):
        self.position = np.array([[27,3],[27,4],[27,5],[28,3],[28,4],[28,5],[29,3],[29,4],[29,5]])
        self.liveLost=time.time()
        self.symbol = np.array(['O','/','|','|','\\','|','/','|','|'])
        self.shield=1
    def activateShield(self,time):
        self.symbol = np.array(['O','/','|','|','\\','|','/','|','|'])
        self.shield=1
        self.lastTime=time
    def deactivateShield(self):
        self.symbol = np.array([' ','O',' ','[','|','\\',' ','/','|'])
        self.shield=0
