import numpy as np
class coin:
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n,m+1]])
        self._symbol = np.array(['$','$'])
        self._name='coin'
    def vanish(self):
        self._position = np.array([[0,0],[0,0]])
        return  
    def write(self):
        self._position[:,1]=self._position[:,1]-1
        return 
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name
