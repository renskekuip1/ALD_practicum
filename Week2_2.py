"""
Class myStack

Implentatie van een Stack met FIFO methode

Parameters:
a : list
    de lijst waarin de stack wordt opgeslagen
tail: int
    grootte van de stack (len(a))

"""
class myStack(list):
    a = []

    def __init__(self,a=[]):
        list.__init__(self,a)
        self.tail = len(a)

    def _pop(self):
        self.tail -= 1
        return self.pop()

    def push(self, x):
        print("Push")
        self.append(x)
        self.tail += 1

    def peek(self):
        print("Peek:", self[self.tail-1])

    def isEmpty(self):
        return self == []

st = myStack()
print("st:", st)
#print("tail: ", st.tail)

print("Empty: ", st.isEmpty())

st.push("1")
print("st:", st)
#print("tail: ", st.tail)

st.peek()
#print("tail: ", st.tail)

print("Empty: ", st.isEmpty())

st.push(2)
print("st:", st)
#print("tail: ", st.tail)

st.push(3)
print("st:", st)
#print("tail: ", st.tail)

print("st.pop:", st._pop())
print("st:", st)
#print("tail: ", st.tail)
