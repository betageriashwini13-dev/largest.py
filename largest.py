import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)