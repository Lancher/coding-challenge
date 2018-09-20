package main

import "fmt"

type Node struct {
    Lo int
    Hi int
    Max int
    Left *Node
    Right *Node
}

type IntervalTree struct {
    root *Node
}

func NewIntervalTree() IntervalTree {
    it := IntervalTree{root:nil}
    it.root = nil
    return it
}


func (it *IntervalTree) Insert(lo int, hi int) {
    it.root = it.insert(it.root, lo, hi)
}

func (it *IntervalTree) insert(node *Node, lo int, hi int) *Node {
    if node == nil {
        new_node := Node{Lo:lo, Hi:hi, Max:hi, Left:nil, Right:nil}
        return &new_node
    }
    if lo <= node.Lo {
        node.Left = it.insert(node.Left, lo, hi)
    } else {
        node.Right = it.insert(node.Right, lo, hi)
    }

    if node.Max < hi {node.Max = hi}
    return node
}

func (it *IntervalTree) Search(lo int, hi int) []Node {
    res := make([]Node, 0)
    it.search(it.root, lo, hi, &res)
    return res
}

func (it *IntervalTree) search(node *Node, lo int, hi int, res *[]Node) {
    if node == nil || node.Max < lo {
        return
    }

    if isIntersection(node, &Node{Lo:lo, Hi:hi}) {
        *res = append(*res, *node)
    }

    if node.Lo < hi {
        it.search(node.Right, lo, hi, res)
    }

    it.search(node.Left, lo, hi, res)
}

func isIntersection(n1 *Node, n2 *Node) bool {
    return n1.Lo < n2.Hi && n2.Lo < n1.Hi
}

// Testing Example:
//
//                 [17, 19]
//               /          \
//              /            \
//        [5, 8]              [21, 24]
//       /     \
//      /       \
// [4, 8]       [15, 18]
//              /      \
//             /        \
//        [7, 10]       [16, 22]
//
//
// Search [21, 23]

func main() {
    it := NewIntervalTree()
    it.Insert(17, 19)
    it.Insert(5, 8)
    it.Insert(4, 8)
    it.Insert(15, 18)
    it.Insert(7, 10)
    it.Insert(16, 22)
    it.Insert(21, 24)
    fmt.Print(it.Search(21, 23))
}


