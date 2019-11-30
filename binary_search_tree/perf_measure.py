import unittest
import time

from consistent_hashing import ConsistentHasher
from bst import BST

class BstTest(unittest.TestCase):

    def test_consistent_hashing(self):

        consistent_hasher = ConsistentHasher(5)
        
        start = time.time()
        for node in range(1, 10):
            consistent_hasher.add_node(node)
        
        end = time.time()
        
        print(end - start)

if __name__ == '__main__':
    unittest.main()