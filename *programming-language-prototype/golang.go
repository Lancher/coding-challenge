package _programming_language_prototype


import "fmt"
fmt.Println("")


import "strconv"
i, _ := strconv.Atoi(exp)
s := strconv.Itoa(-42)


import "sort"

sort.Sort(s[:], func(i, j int) bool {
	return s[i].Lo < s[j].Lo
})

// sort by lex or dict order
sort.Strings(res)


// append two slice
append([]int{1,2}, []int{3,4}...)


// char to ascii
int('a')


// ascii to char
rune(70)


import "strings"

// split to ["1", "e", "l", "l", "o", " ", "W"]
// s[0] == "1",  s[0][0] == 49
s := strings.Split("1ello W", "")
result := strings.Join(s, " ")

// Join
strings.Join(["1", "e", "l", "l", "o", " ", "W"], " ")

// iterate rune
str := "abcd1"
for _, ch := range(str) {
	if 0 <= ch - '0' && ch - '0' <= 9 {
	f	mt.Println("Hello")
	}
}

// lower
str = strings.ToLower(str)
str = strings.ToUpper(str)


// reverse string
func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

// Map need to be init before used
type Data struct{
	M map[string]int
	S []int
	SS [][]int
}


d := Data{M:make(map[string]int)}
d.S = append(data.S, 1)
data.SS = append(data.SS, make([]int, 10))


// pow
import "math"

a := 10
b := 8
math.Pow(float64(a), float64(b))


// Max/Min
const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1


// heap
import (
	"container/heap"
	"fmt"
	)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

h := &IntHeap{2, 1, 5}
heap.Init(h)
heap.Push(h, 3)
fmt.Printf("minimum: %d\n", (*h)[0])
for h.Len() > 0 {
	fmt.Printf("%d ", heap.Pop(h))
}