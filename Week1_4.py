import random

"""


Parameters
----------

Return
------

"""
def create_list(len):
    tmp = []
    for i in range(len):
        tmp.append(random.randrange(1, 365))
    return tmp

"""


Parameters
----------

Return
------

"""
def check_list(a):
    check = False
    length = len(a)
    for nr in range(length):
        x = a[nr]
        b = a.count(x)
        if b > 1:
            check = True
    return check


checksum = 0
for i in range(100):
    i = create_list(23)
    #print(i)
    b = check_list(i)
    if (b == True):
        checksum+=1

print("Percentage: {}".format(checksum))


