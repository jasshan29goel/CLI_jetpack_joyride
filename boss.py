import numpy as np
class boss:
    def __init__(self,n,m):
        self._name='enemy'
        self._lives=5
        self._oscillate=1
        list1 =[]
        list2 =[]
        with open("./ascii_art/boss") as obj:
            i=0
            for line in obj:
                for j in range(len(line)):
                    if line[j] == '0':
                        list1.append([i+n,j+m])
                        list2.append('0')
                i+=1
        
        self._position = np.array(list1)
        self._symbol = np.array(list2)
        self._defense=0
    def write_right(self):
        self._position[:,1]=self._position[:,1]-1
        return 
    def write_up_down(self):
        if self._position[0][0]>=7:
            self._oscillate=-1
        if self._position[0][0]<=2:
            self._oscillate=1
        self._position[:,0]=self._position[:,0]+self._oscillate
        return 
    def position(self):
        return self._position
    def symbol(self):
        return self._symbol
    def name(self):
        return self._name
    def defense(self):
        return self._defense
    def setdefense(self,k):
        self._defense=k
    def lives(self):
        return self._lives
    def setlives(self,k):
        self._lives+=k
    def position00(self):
        return self._position[0][0]
    def position01(self):
        return self._position[0][1]