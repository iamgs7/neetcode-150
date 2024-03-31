from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
        return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally
        or vertically. You may assume all four edges of the grid are all surrounded by water.
        """
        if not grid:
            return 0  # If the grid is empty, return 0

        islands_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                islands_count += self.navigate(grid, row, col)

        return islands_count

    def navigate(self, grid: List[List[str]], row: int, col: int) -> int:
        """
        Recursively navigate the grid and mark visited land cells as '0'.
        Returns 1 if a new island is found, 0 otherwise.
        """
        # Check if the current cell is out of bounds or is water
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[row])
            or grid[row][col] == "0"
        ):
            return 0

        # Mark the current cell as visited
        grid[row][col] = "0"

        # Recursively navigate to neighboring cells
        self.navigate(grid, row, col + 1)
        self.navigate(grid, row, col - 1)
        self.navigate(grid, row + 1, col)
        self.navigate(grid, row - 1, col)

        return 1
