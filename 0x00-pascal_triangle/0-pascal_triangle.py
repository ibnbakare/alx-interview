#!/usr/bin/python3

'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
# '''A module for working with Pascal's triangle.
# '''

# def pascal_triangle(n):
#     '''Creates a list of lists of integers representing
#     the Pascal's triangle of a given integer.
#     '''
#     res = [[1]]
#     for i in range(n -1):
#         temp = [0] + res[-1] + [0]
#         row = []
#         for j in range(len(res[-1]) + 1):
           
#             row.append(temp[j] +temp[j +1])
#         res.append(row)
#     return res
