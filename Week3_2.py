class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyCircLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        if not self.tail:
            return s
        current = self.tail.next
        if current != None:
            s = s + str(current)
            current = current.next
        while current != s[0]:
            if str(current) == s[0]:
                return s
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    """
    Adds given parameter E at the end of list as a node
    """
    def addLast(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,self.tail)
            self.tail.next = self.tail
        else:
            t = ListNode(e, self.tail.next)

            self.tail.next = t
            self.tail = t

    """
    Deletes node that contains given parameter E
    """
    def delete(self,e):
        if self.tail: # self.tail!= None:
            if self.tail == self.tail.next:
                self.tail = None
            else:
                current = self.tail
                while current.next != None and current.next.data != e:
                    current = current.next
                    #not right data -> shift

                if current.next != None:
                    current.next = current.next.next
                    #if right data -> replace

                if current.next == self.tail.next:
                    self.tail = current
                    #last in list -> replace tail

if __name__ == '__main__':
    mylist =  MyCircLinkedList()
    #print(mylist)
    mylist.addLast(1)
    print("Mylist:", mylist)
    mylist.addLast(2)
    print("Mylist:", mylist)
    mylist.addLast(3)
    print("Mylist:", mylist)
    mylist.addLast(4)
    print("Mylist:", mylist)
    mylist.delete(2)
    print("deleted 2:", mylist)
    mylist.delete(1)
    print("deleted 1:", mylist)
    mylist.delete(4)
    print("deleted 4:", mylist)
    mylist.addLast(2)
    print("Added 2:", mylist)
    mylist.delete(3)
    print("deleted 3:", mylist)
