# LEETCODE@ 249. Group Shifted Strings
#
# --END--


def groupStrings(self, strings):
    d = {}
    for string in strings:
        steps = - (ord(string[0]) - 97)
        key_string = ''
        for i in range(len(string)):
            key_string += chr((ord(string[i]) - 97 + steps) % 26 + 97)
        if key_string in d:
            d[key_string].append(string)
        else:
            d[key_string] = [string]

    result = []
    for val in d.values():
        result.append(val)
    return result
