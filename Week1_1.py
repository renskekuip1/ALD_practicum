"""
Function for finding the max in a list

Parameters
----------
a: list
    a given list with at least one element
maxNr: int

"""
def mymax(a):
    maxNr = a[0]
    for i in a:
        assert isinstance(i, int), "Not an number"
        if i > maxNr:
            maxNr = i
    return maxNr

a = [1, 45, 65, -76 , -3]
b = mymax(a)
print(b)
