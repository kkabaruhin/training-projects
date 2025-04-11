class LRUCache:
    class DLNode:
        def __init__(self, key = None, val = None, next = None, prev = None):
            self.next = next
            self.prev = prev
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.ht = {}
        self.cap = capacity
    def prnt(self):
        for key, val in self.ht.items():
            print('(', key, ',', val.val, ')', end='')
        print()

    def get(self, key: int) -> int:
        if (key in self.ht):
            if (self.ht[key].next == None):
                self.prnt()
                return self.ht[key].val


            if (self.ht[key].prev != None):
                self.ht[key].prev.next = self.ht[key].next
            if (self.ht[key].next != None):
                self.ht[key].next.prev = self.ht[key].prev
            self.ht[key].next = None
            self.ht[key].prev = self.head
            self.head.next = self.ht[key]
            self.head = self.ht[key]
            self.prnt()
            return self.ht[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if (key in self.ht):
            self.ht[key].value = value
            if (self.ht[key].next == None):
                self.prnt()
                return

            if (self.ht[key].prev != None):
                self.ht[key].prev.next = self.ht[key].next
            if (self.ht[key].next != None):
                self.ht[key].next.prev = self.ht[key].prev
            self.ht[key].next = None
            self.ht[key].prev = self.head
            self.head.next = self.ht[key]
            self.head = self.ht[key]
            self.prnt()
        else:
            if (self.head == None):
                self.head = self.DLNode(key, value)
                self.tail = self.head
                self.ht[key] = self.head
                self.prnt()
                return
            newNode = self.DLNode(key, value)
            self.head.next = newNode
            newNode.prev = self.head
            self.head = newNode
            self.ht[key] = self.head
            if (self.cap < len(self.ht)):
                tailNext = self.tail.next
                del self.ht[self.tail.key]
                self.tail = tailNext
                self.tail.prev = None
            self.prnt()

sol = LRUCache(2)
sol.put(1,1)
sol.put(2,2 )
print(sol.get(1))
sol.put(3,3)
print(sol.get(2))
sol.put(4,4)
print(sol.get(1))
print(sol.get(3))
print(sol.get(4))