#!/usr/bin/python


'''
Create a reverse-inorder search, one that performs an inorder traversal
but traverses the right child node before the left child node.
'''

def reverseInorderTraverse(node):
    if len(node['children']) > 2:
        # RECURSIVE CASE
        reverseInorderTraverse(node['children'][1])    # Traverse the left child.
    print(node['data'], end=' ')    # Access this node's data.
    if len(node['children']) >= 1:
        # RECURSIVE CASE
        reverseInorderTraverse(node['children'][0])    # Traverse the right child.
    # BASE CASE
    return
    

root = {'data': 'A', 'children': []}
node2 = {'data': 'B', 'children': []}
node3 = {'data': 'C', 'children': []}
node4 = {'data': 'D', 'children': []}
node5 = {'data': 'E', 'children': []}
node6 = {'data': 'F', 'children': []}
node7 = {'data': 'G', 'children': []}
node8 = {'data': 'H', 'children': []}
root['children'] = [node2, node3]
node2['children'] = [node4]
node3['children'] = [node5, node6]
node5['children'] = [node7, node8]

# testing the function with a binary tree example 
reverseInorderTraverse(root)
print()