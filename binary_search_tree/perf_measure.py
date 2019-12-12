import unittest
import time

from consistent_hashing import ConsistentHasher
from bst import BST

class BstTest(unittest.TestCase):

    def test_consistent_hashing(self):

        n = [0, 10000, 30000, 50000, 70000, 90000]

        for i in n:     
            consistent_hasher = ConsistentHasher(5)   
            start = time.time()
            for node in range(1, i):
                consistent_hasher.add_node(node)        
            end = time.time()
            print("n = ", i, ", \t time = ", (end - start))
        
        # print("###########\n\n")
        
        # consistent_hasher = ConsistentHasher(5)   
        # for node in range(1, 2000):
        #     start = time.time()
        #     consistent_hasher.add_node(node)        
        #     end = time.time()
        #     print(end-start)

if __name__ == '__main__':
    unittest.main()