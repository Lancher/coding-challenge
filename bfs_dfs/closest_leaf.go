// LEETCODE@ 742. Closest Leaf in a Binary Tree
//
// --END--


package bfs_dfs



func findClosestLeaf(root *TreeNode, k int) int {
	// dfs find the parent
	parent := make(map[*TreeNode]*TreeNode)
	start := dfs(root, &parent, k)

	// bfs
	queue := make([]*TreeNode, 0)
	queue = append(queue, start)
	vst := make(map[*TreeNode]int)
	vst[start] = 1

	for 0 < len(queue) {
		sz := len(queue)
		for 0 < sz {
			sz -= 1

			// pop node
			cur := queue[0]
			queue = queue[1:]

			// find the leaf
			if cur.Left == nil && cur.Right == nil { return cur.Val }
			// append left node
			if cur.Left != nil {
				if _, ok := vst[cur.Left]; !ok {
					queue = append(queue, cur.Left)
					vst[cur.Left] = 1
				}
			}
			// append right node
			if cur.Right != nil {
				if _, ok := vst[cur.Right]; !ok {
					queue = append(queue, cur.Right)
					vst[cur.Right] = 1
				}
			}
			// append parent
			if _, ok := parent[cur]; ok {
				if _, good := vst[parent[cur]]; !good {
					queue = append(queue, parent[cur])
					vst[parent[cur]] = 1
				}
			}
		}

	}

	return -1
}

func dfs(node *TreeNode, parent *map[*TreeNode]*TreeNode, target int) *TreeNode {
	if node == nil { return nil }

	if node.Val == target { return node }

	// go left
	if node.Left != nil {
		(*parent)[node.Left] = node
		back := dfs(node.Left, parent, target)
		if back != nil { return back }
	}

	// go right
	if node.Right != nil {
		(*parent)[node.Right] = node
		back := dfs(node.Right, parent, target)
		if back != nil { return back }
	}

	return nil
}
