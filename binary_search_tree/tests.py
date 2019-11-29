import unittest

from consistent_hashing import ConsistentHasher
from bst import BST

class BstTest(unittest.TestCase):

    def test_consistent_hashing(self):
        keys = ["abcd", "xyza", "pqrs", "wxyz", "mnop", "defg", "gred", "ojfew", "wejfnv", "dgerfg", "ierhgj",
                "srgergh", "ojrfi", "podjf", "powe"]
        nodes = ["A", "B", "C", "D"]

        consistent_hasher = ConsistentHasher(5)
        for node in nodes:
            consistent_hasher.add_node(node)
            print('\nAdded node %s with hashed ID %d\n' % (node, consistent_hasher.hash(node)))

        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            #print('Key %s was assigned to node %s' % (key, node_id))
            print('\nAdded node %s ' % (key))

        node_to_remove = "B"
        consistent_hasher.remove_node(node_to_remove)
        print('\nRemoved node %s \n' % (node_to_remove))

        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))

        node_to_add = "B"
        consistent_hasher.add_node(node_to_add)
        print('\nAdded node %s' % (node_to_add))

        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))

if __name__ == '__main__':
    unittest.main()