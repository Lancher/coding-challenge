# LEETCODE@ 642. Design Search Autocomplete System
#
# --END--


import collections


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = {}
        self.input_cur = self.root
        self.input_sentence = ''

        # build the trie
        for i in range(len(sentences)):
            self.add_sentence(sentences[i], times[i])

    def add_sentence(self, sentence, time, incr=False):
        cur = self.root
        for ch in sentence:
            if ch not in cur:
                cur[ch] = {}
                # Use the dict to memorize the frequency of words
                cur[ch + '_dict'] = collections.defaultdict(int)
            if incr:
                cur[ch + '_dict'][sentence] += 1
            else:
                cur[ch + '_dict'][sentence] = time
            cur = cur[ch]

    def input(self, c):
        if c == '#':
            self.add_sentence(self.input_sentence, 1, True)
            # reset input_ variables
            self.input_cur = self.root
            self.input_sentence = ''
            return []
        else:
            self.input_sentence += c
            if c not in self.input_cur:
                # sentence is broken, so the following character will not have match.
                self.input_cur = {}
                return []
            else:
                hot = []
                # Use one line to sort the dict !!!!!
                for k, v in sorted(self.input_cur[c + '_dict'].items(), key=lambda p: (-p[1], p[0])):
                    hot.append(k)
                    if len(hot) == 3:
                        break
                self.input_cur = self.input_cur[c]
                return hot
