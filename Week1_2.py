"""
Finds the numbers in a string

Parameters
----------
b : list
    Empty list for found numbers
lastInt : bool
    Parameter as check if the last read number was an int
    If True, current number must be added to last

Return
------

"""
def getNumbers(a):
    b = []
    lastInt = False
    for ch in a:
        if (ch.isdigit() == True):
            ch = int(ch)
            if lastInt == True:
                b[-1] = (b[-1] * 10) + ch
            else:
                b.append(ch)
                lastInt = True
        else:
            lastInt = False

    return b


a = '12een123zin45 6met-632meerdere+7777getallen14'
list = getNumbers(a)
print(list)
