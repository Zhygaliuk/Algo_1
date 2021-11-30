import self as self


class HashTable:
    self.percent = 0.75

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_value(self, key, value):
        hash_key = hash(key) % self.size
        bucket = self.hash_table[hash_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def recive(self):
        use_bucket_cout = 0
        for i in self.hash_table:
            if len(i) != 0:
                use_bucket_cout += 1
        return use_bucket_cout

    def add(self ):
        use = self.recive()
        size = self.size * self.percent
        if use >= size:
            self.size = self.size * 2
            for j in range(0, int(self.size / 2)):
                self.hash_table.append([])

    def get_value(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hash_table[hash_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No found"

    def delete_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(i)
        return

    def show_hashtable(self):
        print(self.hash_table)


if __name__ == '__main__':
    hash_table = HashTable(6)
    hash_table.set_value(1, 24)
    hash_table.set_value(2, 21)
    hash_table.set_value(3, 50)
    hash_table.set_value(4, 21)
    hash_table.set_value(5, 21)
    hash_table.show_hashtable()
    hash_table.check()
    print(hash_table.size)
    hash_table.show_hashtable()
