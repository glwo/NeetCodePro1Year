# leftChild of i = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1]
# parent of i = heap[i // 2]

# Min heaps have the smallest value at the root node. The smallest value has the highest priority to be removed.

# Max heaps have the largest value at the root node. The largest value has the highest priority to be removed.
# 1. Structure Property
    # A binary heap is a binary tree that is a complete binary tree, where every single level of the tree is filled completely, except possibly the lowest level nodes, which are filled contiguously from left to right.

# 2. Order Property
    # The order property for a min-heap is that all of the descendents should be greater than their ancestors. In other words, if we have a root with value y, every node in the right and the left sub-tree should have values greater than or equal to y. This is a recursive property, similar to binary search trees.
