package _programming_language_prototype

import "fmt"

// array declaration
[N]Type
[N]Type{value1, value2, ..., valueN}
[...]Type{value1, value2, ..., valueN}

// slice declaration
make([]Type, length, capacity)
make([]Type, length)
[]Type{}
[]Type{value1, value2, ..., valueN}


import "fmt"
fmt.Println("")


fmt.Println(10 / 3)  // 3
fmt.Println(10 / 3)  // 3.3333333


import "strconv"
i, _ := strconv.Atoi(exp)
s := strconv.Itoa(-42)


import "sort"

sort.Slice(s[:], func(i, j int) bool {
	return s[i].Lo < s[j].Lo
})

// sort by lex or dict order
sort.Strings(res)
sort.Ints(s)

//
family := []struct {
	Name string
	Age  int
}{
	{"Alice", 23},
	{"David", 2},
	{"Eve", 2},
	{"Bob", 25},
}

// Sort by age, keeping original order or equal elements.
sort.SliceStable(family, func(i, j int) bool {
	return family[i].Age < family[j].Age
})


// append two slice
append([]int{1,2}, []int{3,4}...)

// map
if val, ok := dict["foo"]; ok {
	//do something here
}

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

//The builtin copy(dst, src) copies min(len(dst), len(src)) elements.


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


func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

// iterate key value mapping
for k, v := range m {
	fmt.Printf("key[%s] value[%s]\n", k, v)
}

// delete key in map
delete(m, key)

// struct const


// golang shift must be uint
1 << uint(a)



// we dont have to init it agian
type Union struct {
	Parent []int
	Size [][]int
}
un := Union{}
un.Parent = append(un.Parent)


fmt.Println(math.Ceil(x))  // 2
fmt.Println(math.Floor(x))  // 1
int(1 / 3)

// Golang Pass slices