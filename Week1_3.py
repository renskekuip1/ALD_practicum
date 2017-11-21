a = [i for i in range(2, 1001)]

def get_prime(array):
    for a in range(2, array[-1]):
        for b in array:
            test = a*b
            if test in array:
                array.remove(test)
    return array

print(a)
beep = get_prime(a)
print(beep)
