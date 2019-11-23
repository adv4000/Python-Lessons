
"""
Recursion Functions

1) privet
2) privet n times
3) Sum  0+1+2+3+4+5
4) Factorial    5! = 1*2*3*4*5 = 120
5) Fibonacci    0,1,1,2,3,5,8,13,21,34,55,89
"""
import sys
sys.setrecursionlimit(3000)


def privet(x):
    if x == 0:
        return
    print("Hello ", str(x))
    privet(x-1)


def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

#print(fido(50))
privet(1999)
