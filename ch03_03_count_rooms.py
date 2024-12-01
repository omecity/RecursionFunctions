#!/usr/bin/python

import sys 

'''
Using the flood fill algorithm, count the number of ``rooms," or
enclosed spaces, in a 2D grid. You can do this by creating nested for
loops that call the flood fill function on each character in the grid if
it is a period, in order to change the periods into hash characters. For
example, the following data would result in the program finding six
places in the grid with periods, meaning there are five rooms (and the
space outside all the rooms).
'''


im = [
        list('...##########....................................'),
        list('...#........#....####..................##########'),
        list('...#........#....#..#...############...#........#'),
        list('...##########....#..#...#..........#...##.......#'),
        list('.......#....#....####...#..........#....##......#'),
        list('.......#....#....#......############.....##.....#'),
        list('.......######....#........................##....#'),
        list('.................####........####..........######')
    ]


HEIGHT = len(im)
WIDTH = len(im[0])


def floodFill(image, x, y, newChar, oldChar=None):
    
    if oldChar == None:
        # oldChar defaults to the character at x, y.
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        # BASE CASE
        return

    image[y][x] = newChar # Change the character.

    # Uncomment to view each step:
    # printImage(image)
    
    # Change the neighboring characters.
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x - 1, y, newChar, oldChar)
        return # BASE CASE


def printImage(image):
    for y in range(HEIGHT):
        # Print each row.
        for x in range(WIDTH):
            # Print each column.
            print(image[y][x], end="")
        print('')
    print('')


def count_rooms(grid):

    room_counter = 0
    # Iterate through every cell in the grid.
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                floodFill(im, x, y, '#')
                room_counter = room_counter + 1

    return room_counter


number_of_rooms = count_rooms(im)
print("The number of room(s):", number_of_rooms)