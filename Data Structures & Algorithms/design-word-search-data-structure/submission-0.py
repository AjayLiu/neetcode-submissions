class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(w: str, node: TrieNode) -> bool:
            if not node:
                return False
            for idx, c in enumerate(w):
                if c == '.':
                    for child in node.children:
                        if dfs(w[idx+1:], child):
                            return True
                    return False
            
                o = ord(c) - ord('a')
                if not node.children[o]:
                    return False

                node = node.children[o]
            return node.word

        return dfs(word, self.root)
            

