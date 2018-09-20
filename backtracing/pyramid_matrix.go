// LEETCODE@ 756. Pyramid Transition Matrix
//
// --END--


package backtracing

import "strings"


func pyramidTransition(bottom string, allowed []string) bool {
	// create mapping
	m := make(map[string][]string)
	for _, a := range(allowed) {
		two, one := a[0:2], a[2:3]
		if _, ok := m[two]; ok {
			m[two] = append(m[two], one)
		} else {
			m[two] = []string{one}
		}
	}

	// check if success
	return checkSuccess(bottom, m)
}

func checkSuccess (bottom string, m map[string][]string) bool {
	if len(bottom) == 1 { return true }

	// check if all two exist
	n := len(bottom)
	for i := 0; i < n - 1; i++ {
		two := bottom[i:i+2]
		if _, ok := m[two]; !ok {
			return false
		}
	}

	// find all next bottoms
	s := make([]string, 0)
	res := make([]string, 0)
	findAllNxtBottom(bottom, 0, m, &s, &res)

	// dfs
	for _, bot := range(res) {
		if checkSuccess(bot, m) { return true }
	}

	return false
}

func findAllNxtBottom (bot string, nxt_i int, m map[string][]string, s *[]string, res *[]string) {
	if len(bot) - 1 == len(*s) {
		*res = append(*res, strings.Join(*s, ""))
	} else {
		for i := nxt_i; i < len(bot) - 1; i++ {
			two := bot[i:i+2]
			for _, one := range(m[two]) {
				*s = append(*s, one)
				findAllNxtBottom(bot, i + 1, m, s, res)
				*s = (*s)[:len(*s)-1]
			}
		}
	}
}