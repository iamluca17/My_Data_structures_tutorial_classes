import numpy as np

class Chaining_Hash_Table:

    def __init__(self):
        self.MAX = 100
        self.array = [[] for i in range(0, self.MAX)]

    def gen_hash(self, key):

        hash = 0
        for c in key:
            hash += ord(c)
        
        return hash % self.MAX
    
    def __getitem__(self, key):

        h = self.gen_hash(key)
        
        for element in self.array[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, data):

        h = self.gen_hash(key)

        found = False
        for it, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0]==key:
                self.array[h][it] = (key, data)
                found = True
                break

        if not found:
            self.array[h].append((key, data))

    def __delitem__(self, key):
        h = self.gen_hash(key)
        
        for it, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                del self.array[h][it]
                break


class Linprobe_Hash_Table:

    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(0, self.MAX)]
        self.toombstone = 'DELETED'

    def gen_hash(self, key):

        hash = 0
        for c in key:
            hash += ord(c)
        
        return hash % self.MAX
    
    def __setitem__(self, key, value):
        
        if(key == self.toombstone):
            raise Exception(f"You can't set an element of key {self.toombstone}")

        found = False
        bucket_it = self.gen_hash(key)

        while self.array[bucket_it]:
            if self.array[bucket_it][0] == key:
                found = True
                break
            bucket_it += 1
        
        if found:
            self.array[bucket_it] = (key, value)
        else:
            bucket_it = self.gen_hash(key)
            while self.array[bucket_it] and self.array[bucket_it][0] != self.toombstone:
                bucket_it +=1
            
            self.array[bucket_it] = (key, value)


    def __getitem__(self, key):

        found = False
        bucket_it = self.gen_hash(key)

        while self.array[bucket_it]:
            if self.array[bucket_it][0] == key:
                found = True
                break
            bucket_it += 1
        if found:
            return self.array[bucket_it]
        else:
            raise Exception("key not found!")
    
    def __delitem__(self, key):

        found = False
        bucket_it = self.gen_hash(key)

        while self.array[bucket_it]:
            if self.array[bucket_it][0] == key:
                found = True
                break
            bucket_it += 1
        if found:
            self.array[bucket_it] = (self.toombstone, None)
        else:
            raise Exception("key not found!")
        
    def debug_print(self):
        for element in self.array:
            print(self.array)
            print('\n')
