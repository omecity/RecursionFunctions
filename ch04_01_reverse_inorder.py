#!/usr/bin/python


'''
Create a reverse-inorder search, one that performs an inorder traversal
but traverses the right child node before the left child node.
'''

def inorderTraverse(node):
    if len(node['children']) >= 1:
        # RECURSIVE CASE
        inorderTraverse(node['children'][0])    # Traverse the left child.
        print(node['data'], end=' ')    # Access this node's data.
        if len(node['children']) >= 2:
            # RECURSIVE CASE
            inorderTraverse(node['children'][1])    # Traverse the right child.
        # BASE CASE
        return