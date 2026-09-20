class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
#use doubly linked list and hashmap
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #our hashmap, map key to node

        #left is least recently uesd, right is most recently used
        self.left, self.right = Node(0,0), Node(0,0) #lru and mru
        self.left.next , self.right.prev = self.right, self.left #set them pointing to e/o

    def remove(self, node): #helper func, remove nodes from list 
        prev , nxt = node.prev , node.next
        prev.next, nxt.prev = nxt, prev #now node is no longer inbetween

    def insert(self, node): #insert at right( most recent )
        prev, nxt = self.right.prev, self.right #have existing node point to new node
        prev.next = nxt.prev = node #point to new node
        node.next, node.prev = nxt, prev #have new node inserted point to original node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) 
            self.insert(self.cache[key]) #make it most recently used 
            return self.cache[key].val #returns the node, so .val returns the val of node
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) #place in hashmap
        self.insert(self.cache[key])#insert into list 

        if len(self.cache) > self.cap: #if exceeds cap, remove lru from list and cache
            lru = self.left.next #because 0 is self.left
            self.remove(lru)
            del self.cache[lru.key] #pulls from key val declared in node

        
