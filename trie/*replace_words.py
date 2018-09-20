# LEETCODE@ 648. Replace Words
#
# --END--


class Trie:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['END'] = {}

    def find_first_word(self, word):
        new_word = ''
        cur = self.root
        for c in word:
            if c in cur:
                new_word += c
                if 'END' in cur[c]:
                    return new_word
                else:
                    cur = cur[c]
            else:
                break
        return ''


class Solution:
    def replaceWords(self, dict, sentence):
        trie = Trie()
        for word in dict:
            trie.add_word(word)

        res = []
        for word in sentence.split(' '):
            if word:
                new_word = trie.find_first_word(word)
                res.append(new_word if new_word else word)

        return ' '.join(res)

