import math
from time import sleep

def function():
    f0 = 0
    f1 = 1
    inp = 'c'
    while inp != 'q':
        sfn = f1 + f0
        print(" sFn = %d" %sfn)
        f0 = f1
        f1 = f1+1
        print("Press c to continue or q to quit")
        inp = input()
    
if __name__=='__main__':
    function()