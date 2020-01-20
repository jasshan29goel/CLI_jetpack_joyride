import numpy as np
class beam:
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n+1,m],[n+2,m],[n+3,m],[n+4,m]])
        self._symbol = np.array(['|','|','|','|','|'])
        self._name='beam'
    def write(self):
        self._position[:,1]=self._position[:,1]-1
        return
    def vanish(self):
        self._position = np.array([[0,0],[0,0],[0,0],[0,0],[0,0]])
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name

class beamVertical(beam):
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n+1,m],[n+2,m],[n+3,m],[n+4,m]])
        self._symbol = np.array(['|','|','|','|','|'])
        self._name='beam'
class beamHorizontal(beam):
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n,m+1],[n,m+2],[n,m+3],[n,m+4]])
        self._symbol = np.array(['-','-','-','-','-'])
        self._name='beam'
class beamDiagnol(beam):
    def __init__(self,n,m):
        self._position = np.array([[n,m],[n+1,m+1],[n+2,m+2],[n+3,m+3],[n+4,m+4]])
        self._symbol = np.array(['\\','\\','\\','\\','\\'])
        self._name='beam'
