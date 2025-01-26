

class Tree_Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, node):

        if not node.parent:
            node.parent = self
            self.children.append(node)
        else:
            print("Node alreadu has a parent")

    def remove_child(self, node):

        if node in self.children:
            self.children.remove(node)
            node.parent = None

    def get_root(self):

        p = self.parent
        while p:
            p = p.parent

        return p

    def get_level(self):

        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
            
        return level
    
    def preorder(self):

        nodes = [self.data]
        for child in self.children:
            nodes.extend(child.preorder())

        return nodes
    
    def postorder(self):
        nodes = []
        for child in self.children:
            nodes.extend(child.postorder())
        nodes.append(self.data)
        return nodes

    def level_order(self):

        queue = [self]
        nodes = []
        while queue:
            current = queue.pop(0)
            nodes.append(current.data)
            queue.extend(current.children)

        return nodes


    def find(self,value):

        if self.data == value:
            return self
        else:
            for child in self.children:
                found = child.find(value)
                if found:
                    return found
                
        return None
    
    def contains(self, value):
        return self.find(value) is not None
    

    def count_nodes(self):
        node_count = 1
        for child in self.children:
            node_count += child.count_nodes()
        
        return node_count
    
    def get_height(self):
        if not self.children:
            return 0
        
        return 1 + max(child.get_height() for child in self.children)

    def get_depth(self, value):

        if self.data == value:
            return 0
        for child in self.children:
            depth = child.get_depth(value)
            if depth != -1:
                depth = depth + 1
        return -1
    
    def move_to(self, new_node):

        if self.parent:
            self.parent.remove(self)
            
        new_node.add_child(self)

    def replace(self, new_node):

        if self.parent:
            index = self.parent.children.index[self]
            self.parent.children[index] = new_node
        self.parent = None

    def get_path(self):
        path = []

        node = self
        while node:
            path.append(node.data)
            node = node.parent
        return path[::-1]
    
    def find_common_ancestor(self, other_node):
        path_self = set(self.get_path())
        for node in other_node.get_path():
            if node in path_self:
                return node
        return None

    def print_tree(self):

        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


if __name__ == "__main__":

    root = Tree_Node("Electronics")

    laptops = Tree_Node("Laptops")
    tvs = Tree_Node("TVs")
    tablets = Tree_Node("Tablets")

    root.add_child(tvs)
    root.add_child(laptops)
    root.add_child(tablets)

    laptops.add_child(Tree_Node("Mac"))
    laptops.add_child(Tree_Node("Thinkpad"))
    laptops.add_child(Tree_Node("Ideapad"))

    tvs.add_child(Tree_Node("Sony"))
    tvs.add_child(Tree_Node("Samsung"))
    tvs.add_child(Tree_Node("LG"))

    tablets.add_child(Tree_Node("Ipad"))
    tablets.add_child(Tree_Node("Samsung Galaxy TabS"))
    tablets.add_child(Tree_Node("Huawei"))

    root.print_tree()

    print(root.preorder())
    print(root.postorder())
    print(root.level_order())

    root.find("Tablets").print_tree()

