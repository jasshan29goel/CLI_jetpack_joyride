import numpy as np
class bullet:
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n,m+1]])
        self.symbol = np.array(['-','>'])
        self.name='bullet'
    def vanish(self):
        self.position = np.array([[0,0],[0,0]])
        return  
    def write(self):
        self.position[:,1]=self.position[:,1]+2
        return 