#This is my implementation of a linked list class and a double linked list class


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_element_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_element_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return
        
        it = self.head
        while it.next:
            it = it.next

        it.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_element_at_end(data)

    def insert_value_at_index(self, i, data):
        if i<0:
            raise Exception("Exception met: Invalid index. Index has to be greater than 0")
            return
        elif i==0:
            self.insert_element_at_beggining(data)
        else:
            it = self.head
            count = 0
            while i-1>count:

                it = it.next
                count += 1
            
            new_node = Node(data, it.next)
            it.next = new_node

    def replace_value_at_index(self, i, data):
        if i<0:
            raise Exception("Exception met: Invalid index. Index has to be greater than 0")
            return
        elif i==0:
            self.head.data = data
        else:
            it = self.head
            count = 0
            while it and i>count:

                it = it.next
                count += 1
            
            it.data = data

    def get_index_of(self, value) -> int:

        it = self.head
        current_index = 0
        length = self.get_length()
        while it.data != value and current_index < length:
            it = it.next
            current_index += 1

        if (it.data != value) and (not current_index < length):
            raise Exception("no matching data element found")
            return
        else:
            return  current_index

    def insert_after_value(self, value, data):

        it = self.head
        while it and it.data != value:
            it = it.next

        if it.data != value:
            raise Exception("no matching data element found")
            return
        
        new_node = Node(data, it.next)
        it.next = new_node

    def remove_by_value(self, value):

        it = self.head
        if it.data == value:
            self.head = it.next
            del it
            return
        
        previous_node = Node(None, None)
        while it and it.data != value:
            previous_node = it
            it = it.next

        if it.data != value:
            raise Exception("no matching data element found")
            return
        
        previous_node.next = it.next
        del it

    def get_length(self):
        count = 0
        it = self.head
        while it:
            count+=1
            it = it.next

        return count
    

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        it = self.head
        llstr = ''

        while it:
            llstr += str(it.data) + '-->'
            it = it.next

        print(llstr)


class Bilink_Node:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

class Double_Linked_List:
    def __init__(self):
        self.head = None

    def insert_element_at_beggining(self, data):
        if self.head:
            node = Bilink_Node(data, None, self.head)
            self.head.previous = node
            self.head = node
        else:
            self.head = Bilink_Node(data, None, None)

    def insert_element_at_end(self, data):

        if self.head is None:
            self.head = Bilink_Node(data, None, None)
            return
        
        it = self.head
        while it.next:
            it = it.next

        it.next = Bilink_Node(data, it, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_element_at_end(data)

    def insert_value_at_index(self, i, data):
        if i<0:
            raise Exception("Exception met: Invalid index. Index has to be greater than 0")
            return
        elif i==0:
            self.insert_element_at_beggining(data)
        else:
            it = self.head
            count = 0
            while i>count:

                it = it.next
                count += 1
            
            new_node = Bilink_Node(data, it.previous, it)
            it.previous.next = new_node

    def replace_value_at_index(self, i, data):
        if i<0:
            raise Exception("Exception met: Invalid index. Index has to be greater than 0")
            return
        elif i==0:
            self.head.data = data
        else:
            it = self.head
            count = 0
            while it and i>count:

                it = it.next
                count += 1
            
            it.data = data

    def get_index_of(self, value) -> int:

        it = self.head
        current_index = 0
        length = self.get_length()
        while current_index < length and it.data != value:
            it = it.next
            current_index += 1

        if (it.data != value) and (not current_index < length):
            raise Exception("no matching data element found")
            return
        else:
            return  current_index

    def insert_after_value(self, value, data):

        it = self.head
        if it.data == value:
            new_node = Bilink_Node(data, self.head, self.head.next)
            self.head.next = new_node

        while it and it.data != value:
            it = it.next

        if it.data != value:
            raise Exception("no matching data element found")
            return
        
        new_node = Bilink_Node(data, it, it.next)
        it.next.previous = new_node
        it.next = new_node

    def remove_by_value(self, value):

        it = self.head

        if it and it.data == value:
            if it.next:
                self.head = it.next
                self.head.previous = None
                del it
                return
            else:
                self.head = None

        while it and it.data != value:
            it = it.next

        if it.data != value:
            raise Exception("no matching data element found")
            return
        elif it.next:
        
            it.previous.next = it.next
            it.next.previous = it.previous
            del it
        else:
            it.previous.next = None
            del it

    def remove_by_index(self, index):

        it = self.head

        if index > (self.get_length() - 1):
            raise Exception("index out of bounds!")
        elif index < 0:
            raise Exception("invalid index!")
        elif index == 0:

            if it.next:
                self.head = it.next
                self.head.previous = None
                del it
            else:
                self.head = None
        else:

            current_index = 0
            while it and current_index<index:
                it = it.next
                current_index += 1

            if it.next:
                it.previous.next = it.next
                it.next.previous = it.previous
                del it
            else:
                it.previous.next = None
                del it

    def get_element_at_index(self, index):

        it = self.head

        if index > (self.get_length() - 1):
            raise Exception("index out of bounds!")
        elif index < 0:
            raise Exception("invalid index!")
        else:

            current_index = 0
            while it and current_index<index:
                it = it.next
                current_index += 1

            return it.data

    def get_length(self):
        count = 0
        it = self.head
        while it:
            count+=1
            it = it.next

        return count
    

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        it = self.head
        llstr = ''

        while it:
            llstr += str(it.data) + '-->'
            it = it.next

        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        it = self.head
        llstr = ''

        while it.next:
            it = it.next
        while it.previous:
            llstr += str(it.data) + '-->'
            it = it.previous
        llstr += str(it.data) + '-->'

        print(llstr)


if __name__ == "__main__":

    dlink = Double_Linked_List()

    dlink.insert_element_at_end("Car")
    dlink.insert_element_at_end("Plane")
    dlink.insert_element_at_end("Tank")


    dlink.print_forward()

    print(dlink.get_element_at_index(0))