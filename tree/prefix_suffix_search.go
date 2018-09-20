// LEETCODE@ 745. Prefix and Suffix Search
//
// --END--


package tree


type TrieNode struct {
	Child map[string]*TrieNode
	Ws []int
	IsEnd bool
}

func NewTrieNode(IsEnd bool) *TrieNode {
	node := TrieNode{ make(map[string]*TrieNode), make([]int, 0), IsEnd}
	return &node
}


// Trie
type Trie struct {
	Root *TrieNode
}

func (t *Trie) AddWord(word string, w int) {
	cur := t.Root
	// add weight to root because word might be ""
	cur.Ws = append(cur.Ws, w)
	for _, ch := range word {
		ch_str := string(ch)
		if _, ok := cur.Child[ch_str]; !ok {
			cur.Child[ch_str] = NewTrieNode(false)
		}
		cur = cur.Child[ch_str]
		// append weight through inserting a word
		cur.Ws = append(cur.Ws, w)
	}
	cur.IsEnd = true
}

func (t *Trie) SearchPrefixWs(word string) []int {
	cur := t.Root
	for _, ch := range word {
		ch_str := string(ch)
		if _, ok := cur.Child[ch_str]; !ok {
			return make([]int, 0)
		}
		cur = cur.Child[ch_str]
	}
	return cur.Ws
}

func NewTrie() Trie {
	t := Trie{}
	t.Root = NewTrieNode(false)
	return t
}

// reverse string
func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

// Word filter
type WordFilter struct {
	PT Trie
	ST Trie
}


func Constructor(words []string) WordFilter {
	wf := WordFilter{NewTrie(), NewTrie()}
	for i, word := range words {
		// Build Prefix Trie
		wf.PT.AddWord(word, i)

		// reverse word
		rWord := Reverse(word)

		// Build Suffix Trie
		wf.ST.AddWord(rWord, i)
	}
	return wf
}


func (this *WordFilter) F(prefix string, suffix string) int {

	prefixWs := this.PT.SearchPrefixWs(prefix)
	suffix = Reverse(suffix)
	suffixWs := this.ST.SearchPrefixWs(suffix)

	// like merge two sorted list
	i, j := len(prefixWs) - 1, len(suffixWs) - 1
	for 0 <= i && 0 <= j {
		if prefixWs[i] == suffixWs[j] {
			return prefixWs[i]
		} else if prefixWs[i] < suffixWs[j] {
			j -= 1
		} else {
			i -= 1
		}
	}
	return -1
}
