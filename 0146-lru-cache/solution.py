class ListNode: 
    def __init__(self, key, val): 
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cache = dict()
        self.capacity = capacity 

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            ret = node.val
            # only 1 node or node is head
            if node == self.head:
                return ret
            # node is in middle 
            elif node.next and node.prev: 
                node.prev.next = node.next 
                node.next.prev = node.prev 
            # node is tail
            elif node.prev: 
                self.tail = node.prev
                self.tail.next = None
                node.prev = None

            node.next = self.head
            self.head.prev = node
            self.head = node

            return ret
        return -1 
        
    def put(self, key: int, value: int) -> None:
        # key already in cache 
        if key in self.cache: 
            self.get(key)
            self.cache[key].val = value
            
        # cache is empty 
        elif not self.head and not self.tail: 
            self.head = ListNode(key, value)
            self.tail = self.head
            self.cache[key] = self.head
        # cache is full
        elif len(self.cache) == self.capacity: 
            # capacity is 1 - replace
            if self.head == self.tail: 
                self.cache.pop(self.head.key)
                self.head = ListNode(key, value)
                self.tail = self.head
                self.cache[key] = self.head
            # capacity > 1 - evict 
            else: 
                self.cache.pop(self.tail.key)
                self.tail = self.tail.prev 
                self.tail.next = None

                temp = self.head
                self.head = ListNode(key, value)
                self.head.next = temp
                temp.prev = self.head
                self.cache[key] = self.head 

                
        # cache is not empty and not full 
        else: 
            node = ListNode(key, value)
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
