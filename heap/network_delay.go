// LEETCODE@ 743. Network Delay Time
//
// --END--


package heap


import "container/heap"


type Pair struct {
	W int
	I int
}

// heap
type PairHeap []Pair

func (h PairHeap) Len() int           { return len(h) }
func (h PairHeap) Less(i, j int) bool { return h[i].W < h[j].W }
func (h PairHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *PairHeap) Push(x interface{}) {
	*h = append(*h, x.(Pair))
}

func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func networkDelayTime(times [][]int, N int, K int) int {
	// build a graph
	g := make(map[int]map[int]int)
	for _, t := range times {
		u, v, w := t[0] - 1, t[1] - 1, t[2]
		if _, ok := g[u]; !ok {
			g[u] = make(map[int]int)
		}
		g[u][v] = w
	}

	// run dijastra lagorithm
	n := N
	dst := make([]int, n)
	for i := 0; i < n; i++ { dst[i] = -1 }

	// init a heap
	h := &PairHeap{Pair{0, K - 1}}
	heap.Init(h)
	dst[K-1] = 0

	// push the starting node to Heap
	for 0 < h.Len() {
		// pop shortest edge
		p := heap.Pop(h).(Pair)
		w, u := p.W, p.I

		// if the node is not visited
		if dst[u] == -1 {
			dst[u] = w
			n -= 1
			if n == 0 { break }
		}

		// put edges to relax the v
		if _, ok := g[u]; ok {
			for v, v_w := range g[u] {
				if dst[v] == -1 {
					heap.Push(h, Pair{w + v_w, v})
				}
			}
		}
	}

	// find the max
	res := 0
	for i := 0; i < N; i++ {
		if dst[i] == -1 {
			return -1
		}
		if res < dst[i] {
			res = dst[i]
		}
	}

	return res
}