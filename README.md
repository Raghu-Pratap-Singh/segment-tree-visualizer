🌳 Segment Tree Visualizer
A versatile Python library for visualizing Static (Array-based) and Dynamic (Pointer-based) Segment Tree data structures using networkx and matplotlib.

💾 Installation
You can install the package directly via pip:

Bash

pip install segment-tree-visualizer
🚀 Usage Guide
The package exposes two main classes that you import directly into your Python scripts.

Key Requirement: Your custom node objects (e.g., STNode or dNode) must have an attribute named attrs that is a list or tuple containing the data you want displayed inside the node.

1. Static Segment Tree Visualization
Use the StaticSegmentTree class for visualizing complete (full) segment trees that are stored in a 1-indexed list or array.

Example: Max Segment Tree
Python

from segment_tree_visualizer import StaticSegmentTree
import math

# -------------------------------------------------------------------
# STEP 1: DEFINE YOUR NODE AND BUILD FUNCTION (REQUIRED)
# -------------------------------------------------------------------
class STNode:
    """Node for the Static Segment Tree. attrs must be a list/tuple."""
    def __init__(self, value):
        self.attrs = [value] # e.g., [Max Value]

def build_max_segment_tree(arr):
    """Builds a 1-indexed list for the visualizer."""
    n = len(arr)
    sg = [None] * (4 * n + 1)
    
    def build(id, l, r):
        if l == r:
            sg[id] = STNode(arr[l])
            return arr[l]
        mid = (l + r) // 2
        left_max = build(2*id, l, mid)
        right_max = build(2*id+1, mid+1, r)
        sg[id] = STNode(max(left_max, right_max))
        return sg[id].attrs[0]

    build(1, 0, n - 1)
    return sg

# -------------------------------------------------------------------
# STEP 2: BUILD AND VISUALIZE
# -------------------------------------------------------------------
arr = [3, 1, 4, 3, 1, 4] 
sglist = build_max_segment_tree(arr)

# Parameters: array_length (N), indexing_start (1), the built list
tree = StaticSegmentTree(n=len(arr), indexing_reference=1, sglist=sglist)
tree.printTree()
2. Dynamic Segment Tree Visualization
Use the DynamicSegmentTree class for visualizing sparse trees built using pointers (node.left, node.right).

Example: Sparse Tree Structure
Python

from segment_tree_visualizer import DynamicSegmentTree

# -------------------------------------------------------------------
# STEP 1: DEFINE YOUR DYNAMIC NODE CLASS (REQUIRED)
# -------------------------------------------------------------------
class dNode:
    """Node for a pointer-based dynamic segment tree."""
    def __init__(self, leftchild=None, rightchild=None, attrs=None):
        self.attrs = attrs if attrs is not None else []
        self.left = leftchild
        self.right = rightchild

# -------------------------------------------------------------------
# STEP 2: BUILD AND VISUALIZE
# -------------------------------------------------------------------
# Manually build a small, sparse structure
root = dNode(attrs=['R', 'Range:0-1M'])
root.left = dNode(attrs=['L1', 'Max=200'])
root.left.left = dNode(attrs=['L2', 'Val=10'])

# Parameters: root node, minimum range (l), maximum range (r)
# The range [l, r] is used to calculate node positions in the graph.
dtree = DynamicSegmentTree(root, l=0, r=1000000)
dtree.printTree()
🔧 Updating the Visualization
Both classes include an update method to redraw the tree efficiently if the underlying structure changes:

Python

# Static Tree Update Example
# (Assumes a new 'new_sglist' has been generated after an update)
tree.update(new_sglist)
tree.printTree()

# Dynamic Tree Update Example
# (Assumes the 'root' node structure has been modified)
dtree.update(root, 0, 1000000)
dtree.printTree()
🌐 Source Code and License
You can view the full source code and contribute to the project on GitHub.

License
Distributed under the MIT License.
