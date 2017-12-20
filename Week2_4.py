a = 16
b = 105
print("A: {}, B: {}" .format(bin(a), bin(b)))

def myBin(n):
    arr = []
    assert n >= 0, "Uncorrect input"
    while n > 0:
        if n%2 == 0:
            arr.append('0')
        else:
            arr.append('1')
        n = n//2
    arr.reverse()
    return arr

def myBinRecursive(n):
    assert n >= 0, "Uncorrect input"
    if n == 0:
       return  ''
    elif n%2 == 0:
        return myBinRecursive(n//2) + '0'
    else:
        return myBinRecursive(n//2) + '1'

print(myBin(b))
print(myBinRecursive(b))
print(myBinRecursive(0))
print(myBinRecursive(158))
print(bin(158))
print(myBinRecursive(5))
