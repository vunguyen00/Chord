import hashlib

# Chord Node class to simulate a single node in the Chord ring
class ChordNode:
    def __init__(self, node_id, m):
        self.node_id = node_id
        self.m = m
        self.successor = None
        self.predecessor = None

    def hash_key(self, key):
        # Generate hash for the key (simulating hash function in Chord)
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** self.m)

    def find_successor(self, key):
        # Simulate finding successor in the Chord ring
        if self.successor:
            if self.successor.node_id > self.node_id:
                if self.node_id < key < self.successor.node_id:
                    return self.successor
            else:
                if key > self.node_id or key < self.successor.node_id:
                    return self.successor
        return self

# Simulate Chord ring with 3 nodes
class ChordRing:
    def __init__(self, m):
        self.m = m
        self.nodes = []

    def add_node(self, node_id):
        new_node = ChordNode(node_id, self.m)
        if self.nodes:
            # Insert the new node into the ring
            new_node.successor = self.nodes[0]
            self.nodes[0].predecessor = new_node
        self.nodes.append(new_node)
        self.nodes.sort(key=lambda x: x.node_id)  # Ensure nodes are sorted by ID

    def find_node(self, key):
        # Find the node responsible for a key
        key_hash = int(key)
        for node in self.nodes:
            if node.node_id == key_hash:
                return node
            if node.node_id > key_hash:
                return node
        return self.nodes[0]  # Wrap around to the first node if not found

# Test case for Chord algorithm
def test_chord():
    chord_ring = ChordRing(m=3)

    # Adding nodes with IDs 0, 3, 7
    chord_ring.add_node(0)
    chord_ring.add_node(3)
    chord_ring.add_node(7)

    key = input()
    responsible_node = chord_ring.find_node(key)

    if responsible_node:
        print(f"Key {key} is managed by node with ID {responsible_node.node_id}")
    else:
        print("No node found for the key.")

# Run the test case
test_chord()
