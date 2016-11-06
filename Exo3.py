class Node:
    def __init__(self, val)
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val
        self.parent = None #is a node
    


# ABR : 
# left.val <= val <= righ.val
class Tree:
    def __init__(self, node)
        self.root = node
  
    def add(self, element):
       new = Node(element)

       if self.root is None :
           self.root = new
        else :
            node = self.root
            while True :
                if element < node.value :
                    #Go left
                    if node.left is None :
                        node.left = new
                        node.parent = node
                        break
                    node = node.left
                else :
                    #Go right
                    if node.right is None :
                        node.right = new
                        node.parent = node
                        break
                    node = node.right
            return new
        
        
    def run(self, element)
        node = self.root
        while node is not None :
            if element == node.value :
                return True
            else :
                return False
