class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    def _get_hash_for(self, key):
        hash = 0
        for ch in str(key):
            hash += ord(ch)
        return hash % self.size

    def __setitem__(self, key, value):
        key_hash = self._get_hash_for(key)
        map_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = [map_value]
            return
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return
                else:
                    self.map[key_hash].append(map_value)
                    return

    def __getitem__(self, item):
        key_hash = self._get_hash_for(item)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == item:
                    return pair[1]
        return None

    def __repr__(self):
        _str = []
        for item in self.map:
            if item is not None:
                for pair in item:
                    for val in pair:
                        _str.append(val)
                    _str.append("|")
        return " ".join(_str)


mapp = HashMap(128)
mapp["Italy"] = "Rome"
mapp["Russia"] = "Moscow"
print(mapp["Russia"])
print(mapp)

