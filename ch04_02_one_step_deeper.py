#!/usr/bin/python


'''
Create a function that, given a root node as an argument, proceeds to
make the tree one level deeper by adding one child node to each leaf
node in the original tree. This function will need to perform a tree
traversal, detect when it has reached a leaf node, and then add one and
only one child node to the leaf node. Be sure not to go on and add a
child node to this new leaf node, as that will eventually cause a stack
overflow.
'''


def preorderTraverse(node):
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            # Traverse child nodes.
            # BASE CASE
            preorderTraverse(child)
    else:
        node['children'] = [{'data': node['data']*2, 'children': []}]
    return


def printRoot(node):
    print(node['data'], end=' ')    # Access this node's data.
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            # Traverse child nodes to print them.            
            printRoot(child)


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


# call the preorderTraverse function on the tree
preorderTraverse(root)

# show the tree in order of preorder traversal
printRoot(root)