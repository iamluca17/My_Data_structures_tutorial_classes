


class Binary_Search_Tree_Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):

        if self.data == data:
            return
        
        if data < self.data:
            
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Search_Tree_Node(data)
        else:
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_Search_Tree_Node(data)

    def in_order_traversal(self):

        nodes = []

        child_node = self
        if child_node.left:
            nodes += child_node.left.in_order_traversal()

        nodes.append(self.data)

        if child_node.right:
            nodes += child_node.right.in_order_traversal()

        return nodes
    
    def delete_node(self, value):

        

        if self.data == value:

            if not self.left and not self.right:
                return None
            
            if not self.left:
                return self.right
            
            if not self.right:
                return self.left
            

            node_to_reorder = self.right.find_min(return_node=True)
            self.data = node_to_reorder.data
            self.right = self.right.delete_node(node_to_reorder.data)
            del node_to_reorder

        elif value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
            else:
                print("Value not contained in tree after root node!")
                return
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
            else:
                print("Value not contained in tree after root node!")
                return
            
        return self

    def search(self, value):

        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                self.right.search(value)
            else:
                return False
            
    def preorder_traversal(self):

        elements = [self.data]

        if self.left:
            elements.extend(self.left.preorder_traversal())

        if self.right:
            elements.extend(self.right.preorder_traversal())
        
        return elements
    
    def postorder_traversal(self):

        elements = []

        if self.left:
            elements.extend(self.left.postorder_traversal())
        
        if self.right:
            elements.extend(self.right.postorder_traversal())

        elements.append(self.data)
        return elements
    
    def find_min(self, return_node:bool = False):
        min = self

        if self.left:
            
            min = self.left.find_min(return_node=True)
        
        if return_node:
            return min
        else:
            return min.data
        
    def find_max(self, return_node:bool = False):
        max = self

        if self.right:
            
            max = self.right.find_max(return_node=True)

        if return_node:
            return max
        else:
            return max.data
    
    
        
    def calculate_sum(self):

        elements = self.in_order_traversal()

        sum = 0
        for i in elements:
            sum += i

        return sum
        



if __name__ == "__main__":
    
    def build_tree(elements):

        root = Binary_Search_Tree_Node(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root

    numbers = [1, 4, 14, 6, 24, 36, 63]
    numbers_tree = build_tree(numbers)

    numbers_tree.delete_node(24)
    print(numbers_tree.in_order_traversal())