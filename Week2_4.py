"""
Functie die de binaire waarde van een integer teruggeeft
Gemaakt als test

Parameters:
n: int
    integer die wordt meegegeven

Return:
binair : char array/string
    een char array/string met de correcte binaire waarde
"""
def myBin(n):
    binair = []
    assert n >= 0, "Uncorrect input"
    while n > 0:
        if n%2 == 0:
            binair.append('0')
        else:
            binair.append('1')
        n = n//2
    binair.reverse()
    return binair

"""
Functie die de binaire waarde van een integer teruggeeft

Parameters:
n: int
    integer die wordt meegegeven

Return:
myBinRecursive : string
    een string met de correcte binaire waarde
"""
def myBinRecursive(n):
    assert n >= 0, "Uncorrect input"
    if n == 0:
       return  ''
    elif n%2 == 0:
        return myBinRecursive(n//2) + '0'
    else:
        return myBinRecursive(n//2) + '1'


for i in range(1, 256):
    a = bin(i)
    b = '0b' + myBinRecursive(i)
    #print("a:", a, "b:", b)
    if a != b:
        print("Fout, niet hetzelfde")
