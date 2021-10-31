# Things learned:
# ord() -> cast char to unicode int
# TrieNode has two variables: Array[A to Z], is_end_of_word identifier


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self._get_node()

    def _get_node(self) -> TrieNode:
        return TrieNode()

    def _char_to_index(self, c: str) -> int:
        return ord(c) - ord("a")

    def insert(self, key: str):
        pointer = self.root

        for c in key:
            index = self._char_to_index(c)
            if not pointer.children[index]:
                pointer.children[index] = self._get_node()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True

    def search(self, key: str) -> bool:
        pointer = self.root

        for c in key:
            index = self._char_to_index(c)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer.is_end_of_word


if __name__ == "__main__":
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
