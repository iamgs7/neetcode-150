from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum area of an island in the given grid.

        Args:
            grid (List[List[int]]): A 2D grid representing the map, where 1 represents land and 0 represents water.

        Returns:
            int: The maximum area of an island in the grid.
        """
        max_area = 0
        curr_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    curr_area = self.navigate(grid, row, col)
                max_area = max(curr_area, max_area)

        return max_area

    def navigate(self, grid: List[List[int]], row: int, col: int) -> int:
        """
        Performs a depth-first search (DFS) to calculate the area of an island starting from the given cell.

        Args:
            grid (List[List[int]]): The 2D grid representing the map.
            row (int): The row index of the starting cell.
            col (int): The column index of the starting cell.

        Returns:
            int: The area of the island starting from the given cell.
        """
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[row])
            or grid[row][col] == 0
        ):
            return 0

        grid[row][col] = 0  # Mark the current cell as visited
        curr_area = 1  # Initialize the area to 1 for the current cell

        # Recursively explore the neighboring cells
        curr_area += self.navigate(grid, row, col + 1)
        curr_area += self.navigate(grid, row, col - 1)
        curr_area += self.navigate(grid, row + 1, col)
        curr_area += self.navigate(grid, row - 1, col)

        return curr_area
