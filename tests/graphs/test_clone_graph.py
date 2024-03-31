import unittest
from graphs.clone_graph import Solution, Node


class TestCloneGraph(unittest.TestCase):

    def test_clone_empty_graph(self):
        solution = Solution()
        cloned_node = solution.cloneGraph(None)
        self.assertIsNone(cloned_node)

    def test_clone_single_node(self):
        node1 = Node(10)
        solution = Solution()
        cloned_node = solution.cloneGraph(node1)
        self.assertEqual(cloned_node.val, 10)
        self.assertEqual(len(cloned_node.neighbors), 0)

    def test_clone_graph_with_cycle(self):
        # Create a graph with a cycle
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)

        node1.neighbors = [node2]
        node2.neighbors = [node3, node1]
        node3.neighbors = []

        solution = Solution()
        cloned_node = solution.cloneGraph(node1)

        # Check if the cloned graph is correct
        self.assertEqual(cloned_node.val, 10)
        self.assertEqual(len(cloned_node.neighbors), 1)
        self.assertEqual(cloned_node.neighbors[0].val, 20)
        self.assertEqual(len(cloned_node.neighbors[0].neighbors), 2)
        self.assertEqual(cloned_node.neighbors[0].neighbors[0].val, 30)
        self.assertEqual(cloned_node.neighbors[0].neighbors[1].val, 10)

    def test_clone_complex_graph(self):
        # Create the original graph
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)
        node5 = Node(50)

        node1.neighbors = [node2]
        node2.neighbors = [node3, node4]
        node4.neighbors = [node5]

        # Clone the graph
        solution = Solution()
        cloned_node = solution.cloneGraph(node1)

        # Check if the cloned graph is correct
        self.assertEqual(cloned_node.val, 10)
        self.assertEqual(len(cloned_node.neighbors), 1)
        self.assertEqual(cloned_node.neighbors[0].val, 20)
        self.assertEqual(len(cloned_node.neighbors[0].neighbors), 2)
        self.assertEqual(cloned_node.neighbors[0].neighbors[0].val, 30)
        self.assertEqual(cloned_node.neighbors[0].neighbors[1].val, 40)
        self.assertEqual(len(cloned_node.neighbors[0].neighbors[1].neighbors), 1)
        self.assertEqual(cloned_node.neighbors[0].neighbors[1].neighbors[0].val, 50)


if __name__ == "__main__":
    unittest.main()
