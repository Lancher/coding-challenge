// LEETCODE@ 761. Special Binary String
//
// 1. 761. Special Binary String
//
// --END--

package bfs_dfs

import (
	"fmt"
	"sort"
)

func makeLargestSpecial(S string) string {

	fmt.Println(S)
	n := len(S)
	cnt := 0
	i, j := 0, 0
	s := make([]string, 0)

	for j < n {
		if S[j] == '1' {
			cnt += 1
		} else {
			cnt -=1
		}

		if cnt == 0 {
			s = append(s, "1" + makeLargestSpecial(S[i+1:j]) + "0")
			i, j = j + 1, j + 1
		} else {
			j += 1
		}
	}

	sort.Strings(s)
	res := ""
	for i := len(s) - 1; i >=0; i-- {
		res += s[i]
	}

	return res
}


