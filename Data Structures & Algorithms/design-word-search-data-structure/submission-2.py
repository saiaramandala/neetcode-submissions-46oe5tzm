class TrieNode:
    def __init__(self):
        self.collection = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.collection:
                cur.collection[c] = TrieNode()
            cur = cur.collection[c]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.collection.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.collection:
                        return False
                    cur = cur.collection[c]
            return cur.endOfWord
            
        return dfs(0, self.root)

            
        
