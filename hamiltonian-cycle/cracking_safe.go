// LEETCODE@ 753. Cracking the Safe
//
// 1. https://www.youtube.com/watch?v=iPLQgXUiU14
//
// 2. This is just like finding a Hamiltonian Path (Visit all nodes once) in a graph, right?
//    Yes, but in this special case, a path is guaranteed to be found.
//
// --END--


package hamiltonian_cycle

import (
	"strings"
	"math"
	"fmt"
)

func crackSafe(n int, k int) string {
	res := make([]string, 0)
	for i := 0; i < n; i++ { res = append(res, "0") }
	vst := make(map[string]int)

	next_node_str := strings.Join(res, "")
	vst[next_node_str] = 1

	traverse_next_node(&res, n, k, int(math.Pow(float64(k), float64(n))), vst)

	return strings.Join(res, "")
}

func traverse_next_node(res *[]string, n int, k int, total int, vst map[string]int) bool {
	if len(vst) == total {
		return true
	}

	for i := 0; i < k; i++ {
		concat_str := string(int('0') + i)
		next_node_str := strings.Join((*res)[len(*res)-n+1:], "") + concat_str

		if _, ok := vst[next_node_str]; !ok {
			fmt.Println(next_node_str)
			*res = append(*res, concat_str)
			vst[next_node_str] = 1
			if traverse_next_node(res, n, k, total, vst) { return true }
			*res = (*res)[:len(*res)-1]
			delete(vst, next_node_str)
		}
	}
	return false
}