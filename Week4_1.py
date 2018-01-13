'''
Separate chaining hashing

- search(self, e)
- insert(self, e)
- delete(self, e)
- rehash(self, new_len)

Use sets, (aantal elementen in alle sets / lengte tabel) !> 0,75
'''
import random

class HashEntry:
    def __init__(self,element):
        self.elementSet = {None}
        self.elementSet = {element}

    def addToEntry(self,e):
        self.elementSet.add(e)

    def remove(self,e):
        if {e} == self.elementSet:
            print('Entry removed')
        if e in self.elementSet:
            self.elementSet.remove(e)
        else:
            return -1

class ChainHashTable:
    def __init__(self):
        self.len = 3
        self.size = 0
        self.used = 0
        self.table = [None]*self.len
        print("len: " + str(self.len))

    def __repr__(self):
        s = '-----------------\n'
        for i in range(self.len):
            if self.table[i] != None:
                for _ in self.table[i].elementSet:
                    s = s + '(' + str(i) + ',' + str(_) + ")\n"
        s = s + 'len: ' + str(self.len) + '\n'
        s = s + 'size: ' + str(self.size) + '\n'
        s = s + 'used: ' + str(self.used) + '\n'
        s = s + '-----------------\n'
        return s

    def getPos(self,e):
        current = hash(e)%self.len
        #added "e not in set"
        #added if-statement
        return current

    def search(self,e):
        #seems alright for now
        current = self.getPos(e)
        if self.table[current] != None and e in self.table[current].elementSet:
            return current
        else:
            return -1

    def rehash(self,newLen):
        if newLen >= self.size:
            oldLen = self.len
            oldTable = self.table

            self.size = 0
            self.used = 0
            self.len = newLen
            self.table = [None]*self.len

            #removed .isActive part
            for i in range(oldLen):
                if oldTable[i] != None:
                    for element in oldTable[i].elementSet:
                        self.insert(element)
            print('rehash: len: ' + str(self.len))
            print(self)

    def insert(self,e):
        current = self.getPos(e)
        #print(current)
        if self.table[current] == None:
            self.table[current] = HashEntry(e)
            self.size += 1
            self.used += 1
        else:
            self.table[current].addToEntry(e)
            self.size += 1
            self.used += 1
        if (self.size/self.len) > 0.75:
            print('Vullinggraad: ', (self.size/self.len))
            self.rehash(2*self.len)
        return current


    def delete(self,e):
        current = self.search(e)
        if current != -1:
            print("delete: ",current, e)
            self.table[current].remove(e)
        self.size -= 1
        return current


if __name__ == '__main__':

    lht = ChainHashTable()
    lht.insert(12.1)
    print(lht)
    lht.insert(23.1)
    print(lht)
    lht.delete(23.1)
    print(lht)
    lht.insert(23.1)
    print(lht)
    print(lht.search(23.1))
    lht.insert(34.1)
    print(lht)
    lht.insert(45.1)
    print(lht)
    lht.delete(23.1)
    print(lht)
    lht.delete(45.1)
    print(lht)
    lht.rehash(5)
    print(lht)

    testTable = ChainHashTable()
    lst = []
    for i in range(200):
        temp = random.uniform(0.0, 1000.0)
        testTable.insert(temp)
        lst.append(temp)

    for i in range(100):
        temp = random.randrange(0, len(lst))
        testTable.delete(lst[temp])
        lst.remove(lst[temp])
            #if testTable.search(temp) != -1:
            #    testTable.delete(temp)
