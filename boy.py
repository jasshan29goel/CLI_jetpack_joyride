import numpy as np
class boy:
    def __init__(self,width,height):
        self.position = np.array([[27,3],[27,4],[27,5],[28,3],[28,4],[28,5],[29,3],[29,4],[29,5]])
        self.symbol = np.array([' ','O',' ','[','|','\\',' ','/','|'])
        self.width=width
        self.height=height
        self.lives=5
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
