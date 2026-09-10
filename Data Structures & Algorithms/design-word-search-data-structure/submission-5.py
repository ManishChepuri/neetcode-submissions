class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word: str, root: TrieNode):
        curr = root
        for i, c in enumerate(word):
            if c == '.':
                return any(self._search(word[i + 1:], curr.children[child]) 
                            for child in curr.children)
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_word