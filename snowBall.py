import numpy as np
import time
class snowBall:
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n+1,m-1],[n+1,m],[n+1,m+1],[n+2,m]])
        self._symbol = np.array(['*','*','*','*','*'])
        self._name='snowBall'

    def vanish(self):
        self._position = np.array([[0,0]])
        self._symbol = np.array([' '])
        return  
    def write(self,k):
        self._position[:,1]=self._position[:,1]-(5-k/4)
        return 
    def position(self):
        return self._position        
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name

