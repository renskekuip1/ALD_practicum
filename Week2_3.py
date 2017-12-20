class myStack(list):
    a = []

    def __init__(self,a=[]):
        list.__init__(self,a)
        self.tail = len(a)

    def _pop(self):
        self.tail -= 1
        return self.pop()

    def push(self, x):
        #print("Push")
        self.append(x)
        self.tail += 1

    def peek(self):
        print("Peek:", self[self.tail-1])

    def isEmpty(self):
        return self == []

"""
Functie die checkt of een haakjes expressie klopt. 
Een openend haakje wordt op een stack gegooid en 
wanneer een sluitend haakje wordt gelezen, 
kijkt hij op de stack of het bijhorende openende haakjes staat.

Parameters:
switcher: dictionary
    dictionary om bij elkaar horende haakjes met elkaar te linken
stack: myStack()
    stack voor het opslaan van haakjes tijdens het checken

Return:
Geen return type, er wordt geprint of het correct is of niet
"""
def check_bracket(st):
    switcher = {
        '>': '<',
        ')': '(',
        ']': '[',
    }
    assert len(st) > 0, "Empty expression"

    stack = myStack()
    for _ in st:
        if _ == ' ':
            continue
        elif _ not in ('>])'):
            stack.push(_)
        else:
            if stack._pop() != switcher.get(_):
                print("Expression not correct")
                return
    print("Expression correct")

expression = "((( < ) >))"
print(expression)

check_bracket(expression)

expression = "((<>)())"
print(expression)

check_bracket(expression)

expression = "[(<>)]( )(( )( ))"
print(expression)

check_bracket(expression)

expression = "( [ )]"
print(expression)

check_bracket(expression)

#expression = ""
#print(expression)

#check_bracket(expression)
