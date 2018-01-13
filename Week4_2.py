'''
Bepaal twee gebroken getallen met dezelfde hash-waarde
MBV dictionary waarin getal + hashwaarde staan
verjaardags-paradox
'''
import random
def search(d, e):
    for i,j in d.items():
        if j == e:
            print("Same")
            print(repr(i), '-', j)
            return True
    return False

def find_hash():
    tmp = {}

    test = float("inf")
    num = random.uniform(0, test)
        if search(tmp, hash(num)) is False:
            dict = {num: hash(num)}
            tmp.update(dict)
            num = random.uniform(0, 1)
            print(repr(num))
    return tmp

if __name__ == '__main__':
    print(find_hash())
