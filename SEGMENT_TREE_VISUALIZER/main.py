import networkx as nx
import matplotlib.pyplot as plt
import math

# this segment tree is built on top of an array
class StaticSegmentTree:
    
    # 0 indexed/ 1 indexed
    # sg is the segment tree containing indexes of nodes
    def __init__(self, n:int, indexing_reference:int, sglist:list):
        # n->length of array
        self.n = n

        self.sg = sglist.copy()
        # create static segment tree
        self.g = nx.Graph()

        # create a map which contains (key = id starting from 1:(tuple of attributes of this node))
        self.Map = {i:[] for i in range(4*n+1)}
        self.pos=  {}

        # call recursive build function with initial width = n//2
        initial = math.log2(self.n)
        if int(initial) == initial:
            # perfect power of 2
            self.width = (2**(int(initial)))//2
        else:
            # take next power of 2
            self.width = (2**(int(initial) + 1))//2

        # CALL BUILD WITH REQUIRED PARAMETERS <<<
        self.__build(self.width, 0, 0, indexing_reference, 0, self.n-1, None)

        
    # build is called on map initialisation and mupdation of map
    def __build(self, currwidth:int, x:int, level:int, id:int, l:int, r:int, parent_id:int):
        # base case of leaf node
        if l==r:
            # create this node and return and also create pos
            self.Map[id] = tuple(self.sg[id].attrs + [(l,r)])
            self.pos[self.Map[id]] = (x,-1*level)
            # create node
            tempnode = tuple(self.Map[id])
            self.g.add_node(tempnode)

            # add edge with parent
            if parent_id is not None:
                self.g.add_edge(self.Map[parent_id], tempnode)
            # return
            return
        

        # create node and traverse till leaf node is reached
        self.Map[id] = tuple(self.sg[id].attrs + [(l,r)])
        self.pos[self.Map[id]] = (x,-1*level)

        tempnode = tuple(self.Map[id])
        self.g.add_node(tempnode)

        if parent_id is not None:
            self.g.add_edge(self.Map[parent_id], tempnode)

        # traverse
        mid = (l+r)//2
        # rightchild
        self.__build(currwidth//2, x+currwidth, level+1, 2*id+1, mid+1,r,id)
        # leftchild
        self.__build(currwidth//2, x-currwidth, level+1, 2*id, l,mid,id)
    def update(self, updatedsglist:list):
        self.sg = updatedsglist.copy()

        # clear old graph + positions + map
        self.g.clear()
        self.pos.clear()
        self.Map = {i: [] for i in range(4*self.n + 1)}

        # rebuild
        self.__build(self.width, 0, 0, 1, 0, self.n - 1, None)

    def printTree(self):

        plt.figure(figsize=(12, 8))  

        # auto-scale size by total nodes 
        total_nodes = len(self.g.nodes)
        base = 1800         # size when nodes are few
        node_size = max(base // math.sqrt(total_nodes), 300)
        

        nx.draw(
            self.g, self.pos,
            with_labels=True,
            node_color=[(1,1,0.3)],
            node_size=node_size,
            edge_color="black",
            width=1,
            font_size=node_size/44
        )
        
        
        plt.axis("off")
        plt.show()



class DynamicSegmentTree:
    
    def __init__(self, root, l:int, r:int):

        # initialize graph
        self.dg = nx.Graph()
        self.pos = {}

        # call recursive build function with initial width = n//2
        initial = math.log2(r)
        if int(initial) == initial:
            # perfect power of 2
            self.width = (2**(int(initial)))//2
        else:
            # take next power of 2
            self.width = (2**(int(initial) + 1))//2
        # call build function   
        self.__build(root, l, r, 0, 0, self.width, None)

    def __build(self, node, l:int, r:int, x:int, level:int, currwidth:int, parent):
        # build current node
        tempnode = tuple(node.attrs + [(l,r)])
        
        # add in graph
        self.dg.add_node(tempnode)

        # update its position
        self.pos[tempnode] = (x, -level)

        # connect edge with parent if parent exists
        if parent is not None:
            # connect edge
            self.dg.add_edge(parent, tempnode)
        
        mid = (l+r)//2
        # traverse left if it has a left child
        if node.left is not None:
            self.__build(node.left, l,mid,x-currwidth, level+1, currwidth//2, tempnode)

        # traverse right if it has a right child
        if node.right is not None:
            self.__build(node.right, mid+1,r,x+currwidth, level+1, currwidth//2, tempnode)
        
    
    # update function should be called to rebuild the diagram after any change in dynamic segment tree
    def update(self, root, l, r):
        # clear old graph
        self.dg.clear()
        self.pos.clear()
        # call build again
        self.__build(root, l, r, 0, 0, self.width, None)

    def printTree(self):
        plt.figure(figsize=(12, 8))  

        # auto-scale size by total nodes 
        total_nodes = len(self.dg.nodes)
        base = 1800         # size when nodes are few
        node_size = max(base // math.sqrt(total_nodes), 300)
        

        nx.draw(
            self.dg, self.pos,
            with_labels=True,
            node_color=[(1,0.6,1)],
            node_size=node_size,
            edge_color="black",
            width=1,
            font_size=node_size/85
        )
        
        
        plt.axis("off")
        plt.show()


