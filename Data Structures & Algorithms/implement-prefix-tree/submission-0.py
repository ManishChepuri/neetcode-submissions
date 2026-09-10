class TrieNode:
    def __init__(self):
        self.children: {str: TrieNode} = {}
        self.is_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if i == len(word) - 1:
                curr.is_word = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if curr.is_word:
                return True
        return False
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, c in enumerate(prefix):
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if i == len(prefix) - 1:
                return True

        