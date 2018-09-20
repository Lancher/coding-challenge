// LEETCODE@ 729. My Calendar I
//
// --END--


package interval_tree

import "sort"

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

// Calendar
type MyCalendar struct {
	it IntervalTree
}


func Constructor() MyCalendar {
	myCal := MyCalendar{it: NewIntervalTree()}
	return myCal
}


func (this *MyCalendar) Book(start int, end int) bool {
	if 0 < len(this.it.Search(start, end)) {
		return false
	} else {
		this.it.Insert(start, end)
		return true
	}
}


// LEETCODE@ 731. My Calendar II
//
// --END--


import "sort"
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

// sort
type byNodeLo []Node

func (s byNodeLo) Len() int {
	return len(s)
}
func (s byNodeLo) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byNodeLo) Less(i, j int) bool {
	return s[i].Lo < s[j].Lo
}


// leetcode
type MyCalendarTwo struct {
	it IntervalTree
}


func Constructor() MyCalendarTwo {
	myCal := MyCalendarTwo{it: NewIntervalTree()}
	return myCal
}


func (this *MyCalendarTwo) Book(start int, end int) bool {
	nodes := this.it.Search(start, end)
	if len(nodes) < 2 {
		this.it.Insert(start, end)
	} else {
		// Sort Method 1
		sort.Sort(byNodeLo(nodes))

		// Sort Method 2
		sort.Slice(nodes[:], func(i, j int) bool {
			return nodes[i].Lo < nodes[j].Lo
		})

		n := len(nodes)
		for i := 0; i < n - 1; i++ {
			if nodes[i+1].Lo < nodes[i].Hi {
				return false
			}
		}
		this.it.Insert(start, end)
	}
	return true
}


//732. My Calendar III
//
// --END--



import "sort"
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


// Interval
type IT struct {
	Index int
	Val int
}


// leetcode
type MyCalendarThree struct {
	it IntervalTree
	maxSoFar int
}


func Constructor() MyCalendarThree {
	myCal := MyCalendarThree{it: NewIntervalTree(), maxSoFar: 0}
	return myCal
}


func (this *MyCalendarThree) Book(start int, end int) int {
	this.it.Insert(start, end)
	nodes := this.it.Search(start, end)

	its := make([]IT, 0)
	for _, node := range(nodes) {
		its = append(its, IT{Index: node.Lo, Val: 1})
		its = append(its, IT{Index: node.Hi, Val: -1})
	}

	// sort by starting point
	sort.Slice(its[:], func(i, j int) bool {
		if its[i].Index == its[j].Index {
			return its[i].Val < its[j].Val
		}
		return its[i].Index < its[j].Index
	})

	// run swipe line algorithm
	maxSoFar := 0
	curMax := 0
	for _, it := range(its) {
		curMax += it.Val
		if maxSoFar < curMax {
			maxSoFar = curMax
		}
	}

	// update the kth max so far
	if this.maxSoFar < maxSoFar {
		this.maxSoFar = maxSoFar
	}
	return this.maxSoFar
}