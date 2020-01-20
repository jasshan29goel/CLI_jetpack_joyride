import numpy as np
class magnet:
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n,m+1],[n,m+2],[n,m+3],[n,m+4]])
        self.symbol = np.array(['N',':',':',':','S'])
        self.name='magnet'
    # def vanish(self):
    #     self.position = np.array([[0,0]])
    #     self.symbol = np.array([' '])
    #     return  
    def write(self):
        self.position[:,1]=self.position[:,1]-1
        return 