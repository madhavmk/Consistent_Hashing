import unittest
import time

from Consistent_Hashing_with_Virtual_Nodes import ConsistentHash

class test_consistent_hashing(unittest.TestCase):

    def test_consistent_hashing(self):

        keys = ["abcd", "xyza", "pqrs", "wxyz", "mnop", "defg", "gred", "ojfew", "wejfnv", "dgerfg", "ierhgj",
                "srgergh", "ojrfi", "podjf", "powe"]
        nodes = ["A", "B", "C", "D"]        

        consistent_hasher = ConsistentHash(1, 5)
        for i in nodes:
            consistent_hasher.add_machine()

        start = time.time()        
        for i in keys:
                consistent_hasher.get_machine(i)
        end = time.time()
     
        print((end - start)/15)

if __name__ == '__main__':
    unittest.main()
