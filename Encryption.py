#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    result=""
    l=len(s)
    sq = math.sqrt(l)
    a=math.floor(sq)
    b=math.ceil(sq)
    
    l2=[]
    for i in range (0,l,b):
        l2.append(s[i:i+b])
    
    for i in range(b):
        for j in range(len(l2)):
            if(i<len(l2[j])):
                result=result+l2[j][i]
        result=result+" "
    

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
