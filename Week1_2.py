def getNumbers(a):
    b = []
    lastInt = 0
    for ch in a:
        try:
            x = int(ch)
            if lastInt == 1:
                b[-1] = (b[-1] * 10) + x
            else:
                b.append(x)
                lastInt = 1
        except:
            lastInt = 0

    return b


a = '12een123zin45 6met-632meerdere+7777getallen14'
list = getNumbers(a)
print(list)
