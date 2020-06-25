# 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
# is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
from typing import List


def exploreIsland(i, j, grid):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
        return
    else:
        grid[i][j] = '#'
    exploreIsland(i,j+1,grid)
    exploreIsland(i+1,j,grid)
    exploreIsland(i-1,j,grid)
    exploreIsland(i,j-1,grid)



def numIslands(grid) -> int:
    islands = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == '1':
                islands +=1
                exploreIsland(i,j,grid)

    return islands