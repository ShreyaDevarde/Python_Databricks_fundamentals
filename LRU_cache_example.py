class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def put(self, key, value):

        item = f"{key}:{value}"

        # Check if key already exists
        for data in self.cache:

            existing_key = data.split(":")[0]

            if existing_key == str(key):
                self.cache.remove(data)
                break

        # Remove least recently used item if cache is full
        if len(self.cache) >= self.capacity:
            self.cache.pop(0)

        # Add new item as most recently used
        self.cache.append(item)

    def get(self, key):

        for data in self.cache:

            existing_key = data.split(":")[0]

            if existing_key == str(key):

                # Move item to most recently used position
                self.cache.remove(data)
                self.cache.append(data)

                return data.split(":")[1]

        return -1

    def display(self):
        print(self.cache)


cache = LRUCache(3)

cache.put(1, "A")
cache.display()

cache.put(2, "B")
cache.display()

cache.put(3, "C")
cache.display()

print("Get Key 2 =", cache.get(2))
cache.display()

cache.put(4, "D")
cache.display()