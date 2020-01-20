import numpy as np
class magnet:
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n,m+1],[n,m+2],[n,m+3],[n,m+4]])
        self._symbol = np.array(['N',':',':',':','S'])
        self._name='magnet'
    # def vanish(self):
    #     self._position = np.array([[0,0]])
    #     self._symbol = np.array([' '])
    #     return  
    def write(self):
        self._position[:,1]=self._position[:,1]-1
        return
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name
    def position20(self):
        return self._position[2][0]
    def position21(self):
        return self._position[2][1]