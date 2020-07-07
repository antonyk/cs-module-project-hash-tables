class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def find(self, key):
        if self.key == key:
            return (self, self.value)
        else:
            cur = self
            while (cur.next):
                cur = cur.next
                if cur.key == key:
                    return (cur, cur.value)
            return None


    def get(self, key):
        # return the node matching with the matching key
        found = self.find(key)
        if (found):
            (node, value) = found
            return value
        else:
            return None


    def put(self, key, value):
        found = None
        cur = self
        if cur.key == key:
            found = cur

        while (found is None and cur.next):
            cur = cur.next
            if cur.key == key:
                found = cur

        if (found is not None):
            found.value = value
        else:
            cur.next = HashTableEntry(key, value)

    def delete(self, key):
        # return a tuple of (deleted value, new head)
        prev = None
        cur = self
        found = None
        if cur.next is None:
            if cur.key == key:
                return (cur.value, None)
            else:
                raise 'No matching key found'

        while (not found and cur.next):
            prev = cur
            cur = cur.next

        if cur.key == key:
            found = cur


    def __len__(self):
        result = 1
        node = self
        while (node.next):
            result += 1
            node = node.next
        return result

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
# fnvsize = 2**32
# FNV_offset_basis = 14695981039346656037
# FNV_prime = 1099511628211


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity = MIN_CAPACITY):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.capacity = capacity
        self.data = [None] * capacity
        self.total_keys = 0 # increment on insert
        self.ops_since_recalc = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return round(self.total_keys / self.capacity)
        # total_keys = 0
        # for item in self.data:
        #     if item:
        #         total_keys = total_keys + len(item)
        # return round(total_keys / self.capacity)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        FNV_offset_basis = 0x811c9dc5
        FNV_prime = 0x01000193
        result = FNV_offset_basis
        if not isinstance(key, bytes):
            key = key.encode("UTF-8", "ignore")
        for b in key:
            result = result * FNV_prime
            # add this for a 32-bit hashing function
            result &= 0xffffffffffffffff
            result = result ^ b
        return result


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        # sbytes = key.encode()
        result = 5381
        for i in key:
            result = (result * 33) + ord(i)
            result &= 0xffffffff  # add this for a 32-bit hashing function
        return result


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        idx = self.hash_index(key)
        slot = self.data[idx]
        if slot:
            slot.add(key, value)
        else:
            self.data[idx] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        pass


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        pass


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
