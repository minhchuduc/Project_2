# Time: 1hour
#!/usr/bin/env python
from pprint import pprint
import time
#Algo:
"""
We create a range(1,N)
go in directions until nothing left
"""

def go_spiral(matrix, start_r, start_c, step):
    if len(numbers) <= 0:
        return

def go_left(matrix, start_r, start_c):
    global N
    col = start_c
    for i in range(N):
        if matrix[start_r][col] == 0:
            matrix[start_r][col] = numbers.pop()
            last_mod = col
        if col > 0:
            col -= 1
    return (start_r, last_mod)

def go_right(matrix, start_r, start_c):
    global N
    col = start_c
    for i in range(N):
        if matrix[start_r][col] == 0:
            matrix[start_r][col] = numbers.pop()
            last_mod = col
        if col < N - 1:
            col += 1
    return (start_r, last_mod)


def go_up(matrix, start_r, start_c):
    global N
    row = start_r
    for i in range(N):
        if matrix[row][start_c] == 0:
            matrix[row][start_c] = numbers.pop()
            last_mod = row
        if row > 0:
            row -= 1
    return (last_mod, start_c)


def go_down(matrix, start_r, start_c):
    global N
    row = start_r
    for i in range(N):
        if matrix[row][start_c] == 0:
            matrix[row][start_c] = numbers.pop()
            last_mod = row
        if row < N - 1:
            row += 1
    return (last_mod, start_c)


def main():
    global N
    N = input('Nhap N: ')
    time_start = time.time()
    N = int(N)

    global numbers
    # Pop pop the tail, we need number increase, so create below list
    numbers = range(N*N, 0, -1)
    # create 2D matrix ,Filled  with 0s
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    #Start coordinate
    last = (0, 0)
    while len(numbers) > 0:
        last = go_right(matrix, last[0], last[1])
        if len(numbers) <= 0: break
        last = go_down(matrix, last[0], last[1])
        if len(numbers) <= 0: break
        last = go_left(matrix, last[0], last[1])
        if len(numbers) <= 0: break
        last = go_up(matrix, last[0], last[1])
#    pprint(matrix)

    # Nice print
    for i in matrix:
        for k in i:
            print k,
        print 

    print time.time() - time_start

if __name__ == "__main__":
    main()
