"""
Functie die de binaire waarde van een integer teruggeeft

Parameters:
n: int
    integer die wordt meegegeven

Return:
myBinRecursive : char array
    een char expressie met de correcte binaire waarde
"""
def myBinRecursive(n):
    assert n >= 0, "Uncorrect input"
    if n == 0:
       return  ''
    elif n%2 == 0:
        return myBinRecursive(n//2) + '0'
    else:
        return myBinRecursive(n//2) + '1'

a = 16
b = 105
print("A: {}, B: {}" .format(bin(a), bin(b)))

print("myBin -> a:", myBinRecursive(a))
print("myBin -> b:", myBinRecursive(b))
print()
print("myBin -> 0", myBinRecursive(0))
print("BIN -> 0", bin(0))
print("myBin -> 158", myBinRecursive(158))
print("BIN -> 158", bin(158))
print("myBinL -> 5", myBinRecursive(5))
print("BIN -> 5", bin(5))
