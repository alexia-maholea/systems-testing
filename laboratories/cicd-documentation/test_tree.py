import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):
    def setUp(self):
        """Set up a simple tree before each test"""
        self.tree = Tree()
        for value in [10, 5, 15, 2, 7, 12, 20]:
            self.tree.add(value)

    def test_find_existing_node(self):
        """Test căutare nod existent"""
        node = self.tree.find(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 7)

    def test_find_non_existing_node(self):
        """Test căutare nod inexistent"""
        node = self.tree.find(99)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
