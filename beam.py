import numpy as np
class beam:
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n+1,m],[n+2,m],[n+3,m],[n+4,m]])
        self.symbol = np.array(['|','|','|','|','|'])
        self.name='beam'
    def write(self):
        self.position[:,1]=self.position[:,1]-1
        return
    def vanish(self):
        self.position = np.array([[0,0],[0,0],[0,0],[0,0],[0,0]])

class beamVertical(beam):
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n+1,m],[n+2,m],[n+3,m],[n+4,m]])
        self.symbol = np.array(['|','|','|','|','|'])
        self.name='beam'
class beamHorizontal(beam):
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n,m+1],[n,m+2],[n,m+3],[n,m+4]])
        self.symbol = np.array(['-','-','-','-','-'])
        self.name='beam'
class beamDiagnol(beam):
    def __init__(self,n,m):
        self.position = np.array([[n,m],[n+1,m+1],[n+2,m+2],[n+3,m+3],[n+4,m+4]])
        self.symbol = np.array(['\\','\\','\\','\\','\\'])
        self.name='beam'
