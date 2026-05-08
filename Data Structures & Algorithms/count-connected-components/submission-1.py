class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]

    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        self.parent[a] = b

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for e in edges:
            a, b = e
            if uf.find(a) != uf.find(b):
                n -= 1
            uf.union(a,b)
        return n
        