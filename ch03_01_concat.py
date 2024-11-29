#!/usr/bin/python

'''
Using the head-tail technique, create a recursive concat() function that
is passed an array of strings and returns these strings concatenated
together into a single string. For example, concat(['Hello', 'World'])
should return HelloWorld.
'''

def concat(str_list):
    if len(str_list) == 0:       # BASE CASE
        return ""
    else:                       # RECURSIVE CASE
        head = str_list[0]
        tail = str_list[1:]
        return head + concat(tail)
    

str = ["Hello", "World"]
print('The concatenation of', str,'is', concat(str))

str = ["Dry", "Bones", "Shall", "Live", "Again"]
print('The concatenation of', str,'is', concat(str))

str = []
print('The concatenation of', str,'is', concat(str))