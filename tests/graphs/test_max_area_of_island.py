import unittest
from graphs.max_area_of_island import Solution


class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_grid(self):
        grid = []
        expected_output = 0
        self.assertEqual(self.solution.maxAreaOfIsland(grid), expected_output)

    def test_single_cell_island(self):
        grid = [[1]]
        expected_output = 1
        self.assertEqual(self.solution.maxAreaOfIsland(grid), expected_output)

    def test_no_islands(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_output = 0
        self.assertEqual(self.solution.maxAreaOfIsland(grid), expected_output)

    def test_multiple_islands(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        expected_output = 4
        self.assertEqual(self.solution.maxAreaOfIsland(grid), expected_output)

    def test_large_grid(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        expected_output = 6
        self.assertEqual(self.solution.maxAreaOfIsland(grid), expected_output)


if __name__ == "__main__":
    unittest.main()
