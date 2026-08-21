class TrieNode: 
    def __init__(self, val): 
        self.val = val
        self.next = [None] * 26
        self.eow = False

class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        current = self.root
        for char in word: 
            if current.next[ord(char) - ord("a")]: 
                current = current.next[ord(char) - ord("a")]
            else: 
                current.next[ord(char) - ord("a")] = TrieNode(char)
                current = current.next[ord(char) - ord("a")]
        current.eow = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word: 
            if not current.next[ord(char) - ord("a")]:
                return False
            current = current.next[ord(char) - ord("a")]
        return current.eow

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix: 
            if not current.next[ord(char) - ord("a")]: 
                return False
            current = current.next[ord(char) - ord("a")]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
