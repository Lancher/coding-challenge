// LEETCODE@ 839. Similar String Groups
//
// --END--


func numSimilarGroups(A []string) int {
	if len(A) == 0 { return 0 }

	// init
	n := len(A)
	un := NewUnion(n)

	// nested loop
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if similar(A[i], A[j]) {
				un.Union(i, j)
			}
		}
	}

	// return connected number
	return un.ConnN
}

// similar
func similar(a string, b string) bool {
	cnt := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] { cnt += 1 }
		if 2 < cnt { return false }
	}
	return true
}

// union find
type Union struct {
	Parent []int
	Size []int
	ConnN int
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
		un.ConnN -= 1
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