'''
Bepaal twee gebroken getallen met dezelfde hash-waarde
MBV dictionary waarin getal + hashwaarde staan
verjaardags-paradox
'''
import random

def find_hash():
    hash_dict = {}

    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    while (hash(x) % (2**32)) != (hash(y) % (2**32)):
        dict = {x: hash(x) % (2**32), y: hash(y) % (2**32)}
        hash_dict.update(dict)

        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
    dict = {x: hash(x) % (2**32), y: hash(y) % (2**32)}
    return dict

if __name__ == '__main__':
    print(find_hash())
    #find_hash()
