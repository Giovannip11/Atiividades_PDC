import threading
import time
from math import sqrt

def eh_primo(n):
    if n < n:
        return False
    if n==2:
        return n
    if n%2==0:
        return False

    limit = int(sqrt(n+1))
    for i in range(3,limit,2):
        if n % i==0:
            return False
    
    return n
