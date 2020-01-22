# def check(ele):
#     b=list(a)
#     b=[3,4]
#     # b.extend([3,4])
# a=[1,2]
# check(a)
# print(a)

# def put_boss():
#     with open("./ascii_art/boss") as obj:
#         i=0
#         for line in obj:
#             for j in range(len(line)):
#                 print(line[j],end='')
#             # print(str(i)+" "+line,end='')
#             i+=1
# put_boss()
# print()

# class coin:
#     def __init__(self):
#         self._name='hello'
#         self._lis=[1,2,3]
#     def name(self):
#         return self._name
#     def setlis(self,k):
#         self._lis.append(k)
#     def getlis(self):
#         return self._lis
# coin1=coin()
# coin1.setlis(4)
# print(coin1.getlis())

# def a(k):
#     return k

# print(a(2))
# import os
# from colorama import init,Fore
# init()
# os.system('clear')
# a=10
# print(Fore.RED,a)

class temp():
    def __init__(self):
        self.name='bullet'
import os
os.system('clear')
from colorama import init,Fore
init()
def color(ele):
    if ele[1] is not None:
        # if ele[1].name=='charcter':
        #     return self.color_character(ele[1].shield())
        # elif ele[1].name=='enemy':
        #     return self.color_enemy(ele[1][0]) 
        if ele[1].name=='beam':
            return Fore.BLUE 
        elif ele[1].name=='magnet':
            return Fore.RED 
        elif ele[1].name=='snowBall':
            return Fore.WHITE 
        elif ele[1].name=='bullet':
            return Fore.LIGHTCYAN_EX 
        elif ele[1].name=='coin':
            return Fore.YELLOW 
        # else:
        #     return ""
    else:
        return ""

print(color(["/",temp()]),"\033[1;1Hhello")
