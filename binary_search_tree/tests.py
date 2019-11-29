import unittest

from consistent_hashing import ConsistentHasher
from bst import BST


class BstTest(unittest.TestCase):

    def test_consistent_hashing(self):
        keys = ["abcd", "xyza", "pqrs", "wxyz", "mnop", "defg", "gred", "ojfew", "wejfnv", "dgerfg", "ierhgj",
                "srgergh", "ojrfi", "podjf", "powe"]
        nodes = ["1.2.3.4", "3.4.5.6", "5.6.7.8", "7.8.9.10"]

        consistent_hasher = ConsistentHasher()
        for node in nodes:
            consistent_hasher.add_node(node)
            print('\nAdded node %s with hashed ID %d\n' % (node, consistent_hasher.hash(node)))


        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))
            print('\nAdded node %s with hashed ID %d\n' % (key, consistent_hasher.hash(key)))


        node_to_remove = "5.6.7.8"
        consistent_hasher.remove_node(node_to_remove)
        print('\nRemoved node %s with hashed ID %d\n' % (node_to_remove, consistent_hasher.hash(node_to_remove)))

        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))

        node_to_add = "5.6.7.8"
        consistent_hasher.add_node(node_to_add)
        print('\nAdded node %s with hashed ID %d\n' % (node_to_add, consistent_hasher.hash(node_to_add)))

        for key in keys:
            node_id = consistent_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))


if __name__ == '__main__':
    unittest.main()