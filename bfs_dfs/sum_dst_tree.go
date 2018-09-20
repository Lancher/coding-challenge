// LEETCODE@ 834. Sum of Distances in Tree
//
// --END--


package bfs_dfs


func sumOfDistancesInTree(N int, edges [][]int) []int {
	// build a graph
	n := N
	g := make([][]int, n)
	for _, edge := range edges {
		g[edge[0]] = append(g[edge[0]], edge[1])
		g[edge[1]] = append(g[edge[1]], edge[0])
	}

	// subtree size
	size := make([]int, n)
	res := make([]int, n)
	vst := make(map[int]bool)

	// find the subtree size & root path sum
	findSubTreeSize(g, &size, &res, 0, 0, vst)

	// run DFS and move from 0 to other nodes
	vst = make(map[int]bool)
	findPathSum(g, &size, &res, res[0], 0, vst, n)

	return res
}

func findSubTreeSize(g [][]int, size *[]int, res *[]int, u int, level int, vst map[int]bool) int {
	(*res)[0] += level
	vst[u] = true
	sum := 0
	for _, v := range g[u] {
		if _, ok := vst[v]; !ok {
			sum += findSubTreeSize(g, size, res, v, level + 1, vst)
		}
	}
	sum += 1
	(*size)[u] = sum
	return sum
}

func findPathSum(g [][]int, size *[]int, res *[]int, sum int, u int, vst map[int]bool, n int) {
	vst[u] = true
	for _, v := range g[u] {
		if _, ok := vst[v]; !ok {
			(*res)[v] = sum + (n - (*size)[v]) - (*size)[v]
			findPathSum(g, size, res, (*res)[v], v, vst, n)
		}
	}
}
