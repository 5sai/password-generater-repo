import sys
import numpy as np
import string
#n=input("password with 8 chracters")
alpha=list(string.ascii_letters) 
#print("password generater")
n=int(input("length of your password :"))
option=input("enter your option y or n :")
len=np.random.randint(0,52,int(n))
l=[]
if option=="y":
    for i in len:
        k=alpha[i]
        l.append(k)
        h="".join(l)
    print(h)
elif option=="n":
    print("thank you")
    sys.exit()
    
else:
    print("success")
