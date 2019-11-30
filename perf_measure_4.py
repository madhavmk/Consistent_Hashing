import unittest
import time

from Consistent_Hashing_with_Virtual_Nodes import ConsistentHash

class test_consistent_hashing(unittest.TestCase):

    def test_consistent_hashing(self):

        start = time.time()

        consistent_hasher = ConsistentHash(1, 5)

        for i in range(1, 10):
            consistent_hasher.add_machine()

        end = time.time()
        
        
        
        print(end - start)

if __name__ == '__main__':
    unittest.main()
