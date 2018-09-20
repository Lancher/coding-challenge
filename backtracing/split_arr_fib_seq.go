// LEETCODE@ 842. Split Array into Fibonacci Sequence
//
// --END--


package backtracing

import "strconv"

func splitIntoFibonacci(S string) []int {
	found := false
	res := make([]int, 0)
	backtracing(S, 0, &found, &res)
	if found {
		return res
	} else {
		return make([]int, 0)
	}
}

func backtracing (str string, i int, found *bool, res *[]int) {
	if *found { return }
	if i == len(str) {
		if 3 <= len(*res) {
			*found = true
		}
	} else {
		if len(*res) < 2 {
			for j := i + 1; j <= len(str); j++ {
				// 0123 is not valid
				if 1 < j - i && str[i:i+1] == "0" { break }
				it, _ := strconv.Atoi(str[i:j])
				// 32bit integer limit
				if it > 2147483647 { break }
				*res = append(*res, it)
				backtracing(str, j, found, res)
				if *found { return }
				*res = (*res)[:len(*res)-1]
			}
		} else {
			sum := (*res)[len(*res)-1] + (*res)[len(*res)-2]
			for j := i + 1; j <= len(str); j++ {
				it, _ := strconv.Atoi(str[i:j])
				// 32bit integer limit
				if it > 2147483647 { break }
				if it != sum { continue }
				*res = append(*res, it)
				backtracing(str, j, found, res)
				if *found { return }
				*res = (*res)[:len(*res)-1]
			}
		}
	}
}