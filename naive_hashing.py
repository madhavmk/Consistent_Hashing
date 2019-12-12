import hashlib
import zlib

class NaiveHasher:

    def __init__(self):
        self.number_of_nodes = 0
        self.id_to_node = []

    # Note: we need a deterministic hash function. Python hashlib's hash() is not deterministic, and will return
    # a different hash value on different runs.

    def hash(self, item, limit=4294967295):
        id_hash = hashlib.sha512(item.encode())
        id_hash_int = int.from_bytes(id_hash.digest(), 'big')
        final_id = id_hash_int % limit
        return final_id

    def hash2(self, item):
        return zlib.adler32(str.encode(item)) & 0xffffffff

    def add_node(self, node_name):
        self.number_of_nodes = self.number_of_nodes + 1
        self.id_to_node.append(node_name)

    def remove_node(self, node_name):
        self.number_of_nodes = self.number_of_nodes -1
        removed = self.id_to_node.index(node_name)
        self.id_to_node.remove(node_name)
        print('Removed %s: %r' % (node_name, removed))
        return removed

    def assign_key_to_node(self, key):
        key_hash_id = self.hash(key)
        assigned_node_id = key_hash_id % self.number_of_nodes
        if assigned_node_id is None:
            print('Failed to assign key %s (hash = %d) to any node!' % (key, key_hash_id))
            return
        # print('Key %s was hashed to value %d, and was assigned to node %s with id %d' % (key, key_hash_id, self.id_to_node[assigned_node_id], assigned_node_id))
        return self.id_to_node[assigned_node_id]