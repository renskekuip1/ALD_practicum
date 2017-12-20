"""
Function for finding the max in a list

Parameters
----------
a: list
    a given list with at least one element
maxNr: int
    at initializing the first element of the given list

Return
------
maxNr: int
    maximum (largest number) of given list
"""
def mymax(a):
    assert len(a) > 0, "ERROR: no list"
    maxNr = a[0]
    for i in a:
        assert isinstance(i, int), "ERROR: not an number"
        if i > maxNr:
            maxNr = i
    return maxNr

a = [1, 45, 65, -76 , -3]
b = mymax(a)
print(b)
