// LEETCODE@ 838. Push Dominoes
//
// --END--


package left_right_deps

import "strings"

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	s := strings.Split(dominoes, "")

	// from left to right, detect R
	lastR := -1
	for i := 0; i < n; i++ {
		if lastR != -1 {
			if s[i] == "R" {
				for j := lastR; j < i; j++ { s[j] = "R" }
				lastR = i
			} else if s[i] == "L" {
				// 1 | 2 3 4 | 5
				if 1 < i - lastR {
					cnt := (i - lastR - 1) / 2
					for j := 0; j < cnt; j ++ { s[lastR+1+j] = "R" }
					for j := 0; j < cnt; j ++ { s[i-1-j] = "L" }
				}
				lastR = -1
			} else if i == n - 1 {
				for j := lastR; j < i + 1; j++ { s[j] = "R" }
			}
		} else {
			if s[i] == "R" {
				lastR = i
			}
		}
	}

	// from right to left, detect L
	lastL := -1
	for i := n - 1; i >= 0; i-- {
		if lastL != -1 {
			if s[i] == "L" {
				for j := lastL; j > i; j-- { s[j] = "L" }
				lastL = i
			} else if s[i] == "R" {
				// 1 | 2 3 4 | 5
				if 1 < lastL - i {
					cnt := (lastL - i - 1) / 2
					for j := 0; j < cnt; j ++ { s[i+1+j] = "R" }
					for j := 0; j < cnt; j ++ { s[lastL-1-j] = "L" }
				}
				lastL = -1
			} else if i == 0 {
				for j := lastL; j >= 0; j-- { s[j] = "L" }
			}
		} else {
			if s[i] == "L" {
				lastL = i
			}
		}
	}

	return strings.Join(s, "")
}
