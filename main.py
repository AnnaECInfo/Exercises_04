# Exercises on singly linked lists

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = SLLNode(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str([node for node in self])

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

# Exercise 1
    def clear(self):
        for node in self:
            node.next = None
        self.head = None

# Exercise 2
    def get_data(self, data):
        for node in self:
            if node.data == data:
                return node
        if data not in self:
            return False

# Exercise 3
    def insert_node(self, prev_node_data, new_node_data):
        for node in self:
            if node.data == prev_node_data:
                new_node = SLLNode(new_node_data)
                new_node.next = node.next
                node.next = new_node
                self.size += 1
        if prev_node_data not in self:
            return False

# Exercise 4
    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.next = None
            self.size -= 1

        prev_node = None
        for current_node in self:
            if current_node.data == data:
                prev_node.next = current_node.next
                current_node.next = None
                self.size -= 1


# Exercises on doubly linked lists, Exercise 5

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            current.prev = current
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str([node for node in self])

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def clear(self):
        for node in self:
            node.next = None
        self.head = None

    def get_data(self, data):
        for node in self:
            if node.data == data:
                return data
            else:
                return False

    def insert_node(self, prev_node_data, new_node_data):
        for node in self:
            if node.data == prev_node_data:
                new_node = DLLNode(new_node_data)
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                self.size += 1
        if prev_node_data not in self:
            return False

    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

        prev_node = None
        next_node = None
        for current_node in self:
            if current_node.data == data:
                prev_node.next = next_node
                next_node.prev = prev_node
                current_node.next = None
                current_node.prev = None
                self.size -= 1


# Exercises on stacks, Exercise 6

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, element):
        new_node = StackNode(element)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):
        if self.tail is None:
            return None
        else:
            to_remove = self.tail
            to_remove.next = None
            to_remove.prev = None
            self.size -= 1
        return to_remove

    def top(self):
        if self.tail is None:
            return None
        else:
            return self.tail

    def size(self):
        return int(self.size)


# Exercises on queues, Exercise 7

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, element):
        new_node = QueueNode(element)
        if self.tail is None:
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            to_remove = self.head
            to_remove.next = None
            to_remove.prev = None
        self.size -= 1
        return to_remove

    def show_left(self):
        if self.head is None:
            return None
        else:
            return self.head

    def show_right(self):
        if self.tail is None:
            return None
        else:
            return self.tail

    def size(self):
        return int(self.size)
