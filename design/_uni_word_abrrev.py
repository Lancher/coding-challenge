# LEETCODE@ 288. Unique Word Abbreviation
#
# --END--


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        self._d = {}
        for word in dictionary:
            abre_word = word
            if len(word) > 2:
               abre_word = word[0] + str(len(word) - 2) + word[-1]

            if abre_word in self._d:
                if word != self._d[abre_word]:
                    self._d[abre_word] = ''
            else:
                self._d[abre_word] = word

    def isUnique(self, word):
        abre_word = word
        if len(word) > 2:
            abre_word = word[0] + str(len(word) - 2) + word[-1]

        if abre_word in self._d:
            if self._d[abre_word] == word:
                return True
            else:
                return False
        else:
            return True
