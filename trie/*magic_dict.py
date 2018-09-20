# LEETCODE@ 676. Implement Magic Dictionary
#
# TODO: there is a trie answer.
#
# --END--


class MagicDictionary:
    def __init__(self):
        self.words = set()
        self.one_dst_words = {}

    def buildDict(self, dict):
        for word in dict:
            self.words.add(word)
            for i in range(len(word)):
                n_word = word[:i] + '*' + word[i + 1:]
                if n_word in self.one_dst_words:
                    self.one_dst_words[n_word] += 1
                else:
                    self.one_dst_words[n_word] = 1

    def search(self, word):
        for i in range(len(word)):
            n_word = word[:i] + '*' + word[i + 1:]
            # [hello, hallo] search 'hello', return true
            if n_word in self.one_dst_words:
                # if the pattern is greater than 1, it means it can come from different words
                if self.one_dst_words[n_word] > 1:
                    return True
                else:
                    # [hello] search 'hello', return False
                    if word not in self.words:
                        return True
        return False