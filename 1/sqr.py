import sys 
import math

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

def calc(sign):
    return int((-b + sign * math.sqrt(b**2 - 4 * a * c)) / (2 * a))

print(calc(1))
print(calc(-1))