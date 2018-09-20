// LEETCODE@ 765. Couples Holding Hands
//
// 1. If in position 2i and 2i +1 there are person from couple u and couple v sitting there, that means that
//    the permutations are going to involve u and v.
//
// 2. The min number of swaps = N - number of connected components.
//
// --END--


package union_find



type Union struct {
	Parent []int
	Size []int
	ConnectedCount int
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
		un.ConnectedCount -= 1
	}
}

func NewUnion(n int) Union {
	un := Union{make([]int, 0), make([]int, 0), n}
	for i := 0; i < n; i++ {
		un.Parent = append(un.Parent, i)
		un.Size = append(un.Size, 1)
	}
	return un
}

func minSwapsCouples(row []int) int {
	n := len(row) / 2
	un := NewUnion(n)
	for i:= 0; i < n; i++ {
		p := row[i*2]
		q := row[i*2+1]
		un.Union(p/2, q/2)
	}

	return n - un.ConnectedCount
}