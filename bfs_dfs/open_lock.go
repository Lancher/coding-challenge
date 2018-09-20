// 752. Open the Lock
//
// --END--


package bfs_dfs

import (
	"fmt"
	"strings"
)

func openLock(deadends []string, target string) int {
	// if 0000 inside deadends
	for _, dead := range(deadends) {
		if "0000" == dead { return -1 }
	}

	// start from 0000
	queue := []string{"0000"}
	vst := map[string]int{"0000": 1}

	// put deadends
	for _, str := range(deadends) {
		vst[str] = 1
	}

	// bfs
	step := 0
	for len(queue) != 0 {
		fmt.Println(queue)
		sz := len(queue)
		for i := 0; i < sz; i++ {
			// pop first element
			str := queue[0]
			queue = queue[1:]

			// check if reach the target
			if str == target { return step }

			// 4 digits and 10 possibilities for each digit
			for j := 0; j < 4; j++ {
				two := make([]string, 0)
				if str[j] == '0' {
					two = append(two, "1")
					two = append(two, "9")
				} else if str[j] == '9' {
					two = append(two, "0")
					two = append(two, "8")
				} else {
					two = append(two, string(int(str[j]) - 1))
					two = append(two, string(int(str[j]) + 1))
				}
				for k := 0; k < 2; k++ {
					str_s := strings.Split(str, "")
					str_s[j] = two[k]
					new_str := strings.Join(str_s, "")
					if _, ok := vst[new_str]; !ok {
						queue = append(queue, new_str)
						vst[new_str] = 1
					}
				}
			}
		}
		step += 1
	}

	return -1
}
