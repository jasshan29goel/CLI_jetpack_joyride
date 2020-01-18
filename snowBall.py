import numpy as np
import time
class snowBall:
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n+1,m-1],[n+1,m],[n+1,m+1],[n+2,m]])
        self.symbol = np.array(['*','*','*','*','*'])
        self.name='snowBall'

    def vanish(self):
        self.position = np.array([[0,0]])
        self.symbol = np.array([' '])
        return  
    def write(self,k):
        self.position[:,1]=self.position[:,1]-(6-k)
        return 
        
        
