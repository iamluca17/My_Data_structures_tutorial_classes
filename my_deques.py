import my_linked_lists as linkl


class Dequeue:

    def __init__(self):
        self.buffer = linkl.Double_Linked_List()

    def append(self, data):
        self.buffer.insert_element_at_end(data)
    
    def append_left(self, data):
        self.buffer.insert_element_at_beggining(data)
    
    def peek(self):
        endpoint = self.buffer.get_length() - 1
        return self.buffer.get_element_at_index(endpoint)
    
    def peek_left(self):
        return self.buffer.get_element_at_index(0)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Deque buffer is already empty!")
        else:
            endpoint = self.buffer.get_length() - 1
            popped = self.buffer.get_element_at_index(endpoint)
            self.buffer.remove_by_index(endpoint)
            return popped

    def pop_left(self):
        if self.is_empty():
            raise Exception("Deque buffer is already empty!")
        else:
            popped = self.buffer.get_element_at_index(0)
            self.buffer.remove_by_index(0)
            return popped

    def get_length(self):
        return self.buffer.get_length()
    
    def get_element_at_index(self, index):
        return self.buffer.get_element_at_index(index)
    
    def get_index_of(self, data):
        return self.buffer.get_index_of(data)
    
    def is_empty(self):
        return self.buffer.get_length() == 0

class Stack:

    def __init__(self):
        self.deque = Dequeue()

    def push(self, element):
        self.deque.append(element)

    def peek(self):
        return self.deque.peek()

    def peek_left(self):
        return self.deque.peek_left()
    
    def pop(self):
        if self.is_empty():
            print("Can't pop from empty stack!")
            return
        else:
            return self.deque.pop()
    
    def get_length(self):
        return self.deque.get_length()
    
    def get_element_at_index(self, index):
        return self.deque.get_element_at_index(index)
    
    def get_index_of(self, data):
        return self.deque.get_index_of(data)
    
    def is_empty(self):
        return self.deque.is_empty()
    
class Queue:

    def __init__(self):
        self.deque = Dequeue()

    def enqueue(self, element):
        self.deque.append_left(element)

    def peek(self):
        return self.deque.peek()

    def peek_left(self):
        return self.deque.peek_left()
    
    def dequeue(self):
        if self.is_empty():
            print("Can't dequeue from empty queue!")
            return
        else:
            return self.deque.pop()
    
    def get_length(self):
        return self.deque.get_length()
    
    def get_element_at_index(self, index):
        return self.deque.get_element_at_index(index)
    
    def get_index_of(self, data):
        return self.deque.get_index_of(data)
    
    def is_empty(self):
        return self.deque.is_empty()

if __name__ == "__main__":

    test_stack = Stack()
    test_queue = Queue()

    test_stack.push("Call 1")
    test_stack.push("Call 2")
    test_stack.push("Call 3")

    print(test_stack.peek())
    print(test_stack.pop())
    print(test_stack.peek())
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())

    test_queue.enqueue("process 1")
    test_queue.enqueue("process 2")
    test_queue.enqueue("process 3")

    print(test_queue.peek())
    print(test_queue.dequeue())
    print(test_queue.peek())
    print(test_queue.dequeue())
    print(test_queue.peek())
    print(test_queue.dequeue())
    print(test_queue.dequeue())