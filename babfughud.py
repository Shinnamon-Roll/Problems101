print(f"-17 mod 2 = {17 % 2}")
print(f"-101 mod 13 = {-101 % 13}")
print(f"144 mod 7 = {144 % 7}")
print(f"199 mod 19 = {199 % 19}")

def ihere(a, b):
    while b != 0:
        a, b = b, a % b
    print(f"ห.ร.ม. of 414 and 622 : {a}")
ihere(414, 622)

print(f"(10111)2 is mean : 16 8 4 2 1 = 1 + 2 + 4 + 16 : {1 + 2 + 4 + 16}")


def isus(a):
    result = []
    for i in range(1,a +1):
        if a % i == 0:
            result.append(i)
    print(f"a | 10 = {result}")
isus(10)

def kuy(a, b):
    tempA = []
    tempB = []
    for i in range(1,a +1):
        if a % i == 0:
            tempA.append(i)
    
    for j in range(1,b +1):
        if a % j == 0:
            tempB.append(j)

    tempA = set(tempA)
    tempB = set(tempB)
    print(f"a|75 and a|125 = {sorted(tempA.intersection(tempB))}")

kuy(75, 125)
    







                
