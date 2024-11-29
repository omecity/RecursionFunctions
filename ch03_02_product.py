#!/usr/bin/python

'''
Using the head-tail technique, create a recursive product() function that
is passed an array of integers and returns the total multiplied product
of them. This code will be almost identical to the sum() function in this
chapter. However, note that the base case of an array with just one inte-
ger returns the integer, and the base case of an empty array returns 1. 

'''

def product(numbers):
    if len(numbers) == 0:       # BASE CASE
        return 1
    else:                       # RECURSIVE CASE
        head = numbers[0]
        tail = numbers[1:]
        return head * product(tail)


nums = []
print('The product of', nums, 'is', product(nums))

nums = [1, 2, 3, 4, 5]
print('The product of', nums, 'is', product(nums))

nums = [1, 10, 100, 1000]
print('The product of', nums, 'is', product(nums))