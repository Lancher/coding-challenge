import collections


def concat_words(strings):
    # strings
    strings = [string.strip().split(' ') for string in strings]

    # "head" -> ids
    head_ids = collections.defaultdict(set)
    for i, string in enumerate(strings):
        head_ids[string].add(i)

    # build graph by ids
    graph = collections.defaultdict(set)



