import unittest

from naive_hashing import NaiveHasher

class NaiveTest(unittest.TestCase):

    def test_consistent_hashing(self):
        keys = ["abcd", "xyza", "pqrs", "wxyz", "mnop", "defg", "gred", "ojfew", "wejfnv", "dgerfg", "ierhgj",
                "srgergh", "ojrfi", "podjf", "powe"]
        nodes = ["A", "B", "C", "D"]

        naive_hasher = NaiveHasher()
        for node in nodes:
            naive_hasher.add_node(node)
            print('\nAdded node %s' % (node))


        for key in keys:
            node_id = naive_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s \n' % (key, node_id))

        node_to_remove = "B"
        naive_hasher.remove_node(node_to_remove)
        print('\nRemoved node %s\n' % (node_to_remove))

        for key in keys:
            node_id = naive_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))

        node_to_add = "B"
        naive_hasher.add_node(node_to_add)
        print('\nAdded node %s \n' % (node_to_add))

        for key in keys:
            node_id = naive_hasher.assign_key_to_node(key)
            print('Key %s was assigned to node %s' % (key, node_id))


if __name__ == '__main__':
    unittest.main()
