// LEETCODE@ 851. Loud and Rich
//
// --END--


package bfs_dfs



func loudAndRich(richer [][]int, quiet []int) []int {
	// init
	n := len(quiet)

	// build graph
	g := make([][]int, n)
	for _, r := range richer {
		g[r[1]] = append(g[r[1]], r[0])
	}

	// run dfs
	res := make([]int, 0)
	for i := 0; i < n; i++ { res = append(res, -1) }
	for i := 0; i < n; i++ {
		if res[i] == -1 {
			dfs(g, quiet, i, &res)
		}
	}

	// return answer
	return res
}

func dfs(g [][]int, quiet []int, node int, res *[]int) int {
	// if node already be visisted, we dont need to do it again
	if (*res)[node] > 0 { return (*res)[node] }
	(*res)[node] = node
	for _, next_node := range g[node] {
		reIdx := dfs(g, quiet, next_node, res)
		if quiet[reIdx] < quiet[(*res)[node]] { (*res)[node] = reIdx }
	}
	return (*res)[node]
}
