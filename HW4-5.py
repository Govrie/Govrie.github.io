class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n'+str(current.value)+'\n'
            while current.next is not None:
                current = current.next
                out += str(current.value)+'\n'
            return out+']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

if __name__ == '__main__':
    L = LinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    print(L)
