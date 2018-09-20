// LEETCODE@ 737. Sentence Similarity II
//
// --END--


package union_find


import "sort"


type Union struct {
	Parent []int
	Size []int
}

func (un *Union) Root(p int) int {
	for p != un.Parent[p] {
		un.Parent[p] = un.Parent[un.Parent[p]]
		p = un.Parent[p]
	}
	return p
}

func (un *Union) Connected(p int, q int) bool {
	return un.Root(p) == un.Root(q)
}

func (un *Union) Union(p int, q int) {
	root_p, root_q := un.Root(p), un.Root(q)
	if root_p != root_q {
		if un.Size[root_p] < un.Size[root_q] {
			un.Parent[root_p] = root_q
			un.Size[root_q] += un.Size[root_p]
		} else {
			un.Parent[root_p] = root_q
			un.Size[root_q] += un.Size[root_p]
		}
	}
}

func NewUnion(n int) Union {
	un := Union{make([]int, 0), make([]int, 0)}
	for i := 0; i < n; i++ {
		un.Parent = append(un.Parent, i)
		un.Size = append(un.Size, 1)
	}
	return un
}

func areSentencesSimilarTwo(words1 []string, words2 []string, pairs [][]string) bool {
	if len(words1) != len(words2) { return false }

	// add all words to the m
	idx := 0
	m := make(map[string]int)
	for _, words := range(pairs) {
		for _, word := range(words) {
			if _, ok := m[word]; !ok {
				m[word] = idx
				idx += 1
			}
		}
	}
	for _, word := range(words1) {
		if _, ok := m[word]; !ok {
			m[word] = idx
			idx += 1
		}
	}
	for _, word := range(words2) {
		if _, ok := m[word]; !ok {
			m[word] = idx
			idx += 1
		}
	}

	// build union find
	n := len(m)
	un := NewUnion(n)

	// start to union
	for _, words := range(pairs) {
		for i := 0; i < len(words) - 1; i++ {
			un.Union(m[words[i]], m[words[i+1]])
		}
	}

	// find parent for each word in words1 and words2
	w1 := make([]int, 0)
	w2 := make([]int, 0)
	for _, word := range(words1) { w1 = append(w1, un.Root(m[word])) }
	for _, word := range(words2) { w2 = append(w2, un.Root(m[word])) }

	// sort
	sort.Slice(w1[:], func (i int, j int) bool { return w1[i] < w1[j] })
	sort.Slice(w2[:], func (i int, j int) bool { return w2[i] < w2[j] })

	// cmp if two slices are indetical
	for i := 0; i < len(w1); i++ {
		if w1[i] != w2[i] { return false }
	}
	return true
}