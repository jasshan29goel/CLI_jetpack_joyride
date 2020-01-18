import numpy as np
class boss:
    def __init__(self,n,m):
        self.name='enemy'
        self.lives=5
        self.oscillate=1
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
        
        self.position = np.array(list1)
        self.symbol = np.array(list2)
    
    def write_right(self):
        self.position[:,1]=self.position[:,1]-1
        return 
    def write_up_down(self):
        if self.position[0][0]>=7:
            self.oscillate=-1
        if self.position[0][0]<=2:
            self.oscillate=1
        self.position[:,0]=self.position[:,0]+self.oscillate
        return 