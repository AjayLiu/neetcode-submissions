class Node:
    def __init__(self, c: char):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not n.children[idx]:
                n.children[idx] = Node(c)
            n = n.children[idx]
        n.isEnd = True

    def search(self, word: str) -> bool:
        n = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not n.children[idx]:
                return False
            n = n.children[idx]
        return n.isEnd

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not n.children[idx]:
                return False
            n = n.children[idx]
        return True
        
        