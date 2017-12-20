def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X", end= " ")
            else:
                print("*", end= " ")
        print()
    print()

def rsearch(N):
    global a, t
    global temp
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                return True # geschikte a gevonden
            else:
                if rsearch(N):  #if TRUE
                    if t <= 12:
                        print("TEMP BEFORE COPY:", temp)
                        temp = a.copy()
                        print("TEMP AFTER COPY:", temp)
                        t += 1
                        return rsearch(N)
                    else:
                        print(a)
                        return rsearch(N)
            del a[-1] # verwijder laatste element
    return False

def rsearch2(N):
    global a
    global b
    for i in range(N):
        if check(a,i) and a not in b:
            #print("v")
            a.append(i)
            if len(a) == N:
                b.append(a)
                print(a)
                rsearch2(N)
            else:
                rsearch2(N)
            del a[-1] # verwijder laatste element
a = [] # a geeft voor iedere rij de kolompositie aan
b = []
t = 0
rsearch2(8)

print("b")
for _ in b:
    print(_)
print("C")

a = [] # a geeft voor iedere rij de kolompositie aan
temp = [] #DEBUG POSSIBILITIES
t = 0

rsearch(8)
print(a)

#temp = a    ; print("A TO TEMP")
#rsearch(8)
#print(a)
#if a != temp:
#    print("WOOP")

#printQueens(a)
