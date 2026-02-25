import random

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
        self.size -= 1
        return current_head

    def add(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1   # ✅ FIXED

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        if self.head is None:
            return "Waitlist Status: Empty."

        return_str = "Waitlist Status:  "
        for node in self:
            return_str += f"{node.data.first_name} {node.data.last_name} -- "
        return return_str.rstrip(" -- ")


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = random.randint(1000, 9999)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ID: {self.student_id}"


if __name__ == '__main__':

    s1 = Student("Mackenzie", "Bingham")
    s2 = Student("Hannah", "Sis")
    s3 = Student("Addie", "Rae")

    waitlist = Queue()

    waitlist.add(s1)
    waitlist.add(s2)
    waitlist.add(s3)

    print(waitlist)
    print("Size is:", waitlist.size)

    while not waitlist.is_empty():
        student_node = waitlist.pop_left()
        print(student_node.data, "has been moved off the waitlist.")
        print(waitlist)
        print("Size is:", waitlist.size)



    
