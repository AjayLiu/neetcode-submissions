class TrieNode:
    def __init__(self):
        self.word = False
        self.children = dict()

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(w: str, node: TrieNode) -> bool:
            if not node:
                return False
            for idx, c in enumerate(w):
                if c == '.':
                    for child in node.children.values():
                        if dfs(w[idx+1:], child):
                            return True
                    return False
            
                if c not in node.children:
                    return False

                node = node.children[c]
            return node.word

        return dfs(word, self.root)
            

