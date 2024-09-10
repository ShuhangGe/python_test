class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False

class trie():
    def __init__(self,root) -> None:
        self.root = root
    def insert(self, keys):
        if self.root is None:
            return 
        cur  = self.root
        for key in keys:
            index = ord(key) - ord('a')
            if cur.child[index] is None:
                new_node = TrieNode()
                cur.child[index] = new_node
            cur = cur.child[index]
        cur.wordEnd = True
    def search(self, keys):
        if self.root is None:
            return 
        cur  = self.root
        for key in keys:
            index = ord(key) - ord('a')
            if cur.child[index] is None:
                return False
            cur = cur.child[index]
        return cur.wordEnd


