# LEETCODE@ 804. Unique Morse Code Words
#
# --END--


def uniqueMorseRepresentations(self, words):
    codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    st = set()
    for word in words:
        s = ''
        for c in word:
            s += codes[ord(c) - ord('a')]
        st.add(s)
    return len(st)
