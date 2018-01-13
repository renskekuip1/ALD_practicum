'''
Uitrekenen hoeveel verschillende manieren van een geldbedrag er zijn

N het bedrag in eurocent
return: aantal manieren waarin betaald

In matrix A is A[i][j] het aantal mogelijkheden waarmee bedrag J beaald
kan worden met de munten m[0] t/m m[i]


'''

def F(n):
    #amount in eurocent
    if n > 10000:
        return None

    a = []
    m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]

    #triangle.append([1]*i)
    for i in range(len(m)):
        if m[i] < n:
            a.append([1]*(n+1))


    for i in range(1, len(a)):
        for j in range(2, len(a[i])):
            if n >= m[i]:
                a[i][j] = a[i-1][j] + a[i][j-m[i]]
            elif n < m[i]:
                a[i][j] = a[i-1][j]

    for line in a:
        print(line)


if __name__ == '__main__':
    debug = F(7)
    print(debug)
