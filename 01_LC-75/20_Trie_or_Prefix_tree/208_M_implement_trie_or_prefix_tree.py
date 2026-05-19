class TrieNode:
    def __init__(self):
        self.mapping = {}
        self.is_end = False
        # will be filled with children (keys) for each insert
        # structure: root[key] = dict(first letter of each children)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # we to first find if the first letters are keys of the subsequent nodes
        """
        start from root, check if first letter is there
        if yes: make that the new node and go to the next letter

        2 possibilities after:
        1. we reach the end of our string: 
        """
        i = 0
        curr_node = self.root
        while i < len(word) and word[i] in curr_node.mapping:
            curr_node = curr_node.mapping[word[i]] # traverse the ith TrieNode
            i += 1
        # we can now verify if we reached the end
        while i < len(word): # means we reached the end of the trienode but still haven't finished traversing the word
            curr_node.mapping[word[i]] = TrieNode()
            curr_node = curr_node.mapping[word[i]]
            i += 1
        # now make that end of word as a valid end
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        # search is easier as we can just take the traversal part of insert
        i = 0
        curr_node = self.root
        while i < len(word) and word[i] in curr_node.mapping:
            curr_node = curr_node.mapping[word[i]]
            i += 1
        return curr_node.is_end and i == len(word) # cause we can reach end of trie without finishing the word

    def startsWith(self, prefix: str) -> bool:
        # same as search but return if we reached end of string regardless if we reached end of trie
        word = prefix
        i = 0
        curr_node = self.root
        while i < len(word) and word[i] in curr_node.mapping:
            curr_node = curr_node.mapping[word[i]]
            i += 1
        return i == len(word) # cause we can reach end of trie without finishing the word


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)