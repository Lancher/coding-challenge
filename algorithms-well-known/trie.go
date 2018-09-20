package main

// Trie Nodes
type TrieNode struct {
	Child map[string]*TrieNode
	IsEnd bool
}

func NewTrieNode(IsEnd bool) *TrieNode {
	node := TrieNode{ make(map[string]*TrieNode), IsEnd}
	return &node
}


// Trie
type Trie struct {
	Root *TrieNode
}

func (t *Trie) AddWord(word string) {
	cur := t.Root
	for _, ch := range word {
		ch_str := string(ch)
		if _, ok := cur.Child[ch_str]; !ok {
			cur.Child[ch_str] = NewTrieNode(false)
		}
		cur = cur.Child[ch_str]
	}
	cur.IsEnd = true
}

func (t *Trie) Search(word string) bool {
	cur := t.Root
	for _, ch := range word {
		ch_str := string(ch)
		if _, ok := cur.Child[ch_str]; !ok {
			return false
		}
		cur = cur.Child[ch_str]
	}
	return cur.IsEnd
}

func (t *Trie) SearchPrefix(word string) bool {
	cur := t.Root
	for _, ch := range word {
		ch_str := string(ch)
		if _, ok := cur.Child[ch_str]; !ok {
			return false
		}
		cur = cur.Child[ch_str]
	}
	return cur.IsEnd
}

func NewTrie() Trie {
	t := Trie{}
	t.Root = NewTrieNode(false)
	return t
}







