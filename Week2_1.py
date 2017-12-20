""""
Functie voor machtsverheffen van a**n

Parameters:
a : int
    base van de berekening
n : int 
    macht
count : int
    telt hoe vaak er vermenigvuldigt is

Return:
m : int
    antwoord van de berekening, indien n = 0 returnt 1 (want a**0 = 1)
"""
def machtv3(a, n):
    count = 1
    m = 1
    while n > 0:
        if n%2 == 0:
        #check of hij even is
            n = n//2
            for _ in range(0, n):
            #vermenigvuldig N aantal keer
                m = m*a
                count+=1
        else:
            n = n-1
            m = m*a
            count+=1
    print("Count: ", count)
    return m

a = 4**0
b = machtv3(4, 0)
print(a, b)

if a == b:
    print("Correct Answer")
else:
    print("Wrong Answer")
