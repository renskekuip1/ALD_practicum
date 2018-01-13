'''
def
 B(n,k):
   return((fac(n)//fac(k))//fac(n-k))

'''
def fac(n):
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)

def B(n, k):
    triangle = []
    n += 1
    for i in range(1, n+1):
        triangle.append([1]*i)
    for i in range(0, n):
        for j in range(len(triangle[i])-1):
            if i > 1 and j > 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
    return triangle[n-1][k]

def f(n,k):
    return((fac(n)//fac(k))//fac(n-k))

test = B(100,50)
print('test=', f(100,50))
print("My func =", test)
if f(100,50) == test:
    print("klopt")
