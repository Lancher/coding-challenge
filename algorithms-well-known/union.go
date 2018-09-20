package main

import "fmt"

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


