import numpy as np
class bullet:
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n,m+1]])
        self._symbol = np.array(['-','>'])
        self._name='bullet'
    def vanish(self):
        self._position = np.array([[0,0],[0,0]])
        self._symbol = np.array([' ',' '])
        return  
    def write(self):
        self._position[:,1]=self._position[:,1]+2
        return 
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name
    def position00(self):
        return self._position[0][0]