class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop_left(self):
        if self.head is None:
            return None
        current_head = self.head
        self.head = self.head.next
        self.size = self.size - 1
        return current_head

    def add(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        self.size = self.size - 1

    def is_empty(self):
        if self.head is not None: return False
        return True

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return_str = "Queue object: "
        for node in self:
            return_str = return_str + node.data + " -- "
        return return_str
        print(repr(my_queue))















        
