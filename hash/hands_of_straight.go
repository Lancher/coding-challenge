// LEETCODE@ 846. Hand of Straights
//
// --END--


package hash

import "sort"

func isNStraightHand(hand []int, W int) bool {
	// count freq
	m := make(map[int]int)
	for _, val := range hand {
		if _, ok := m[val]; ok {
			m[val] += 1
		} else {
			m[val] = 1
		}
	}

	// sort
	keys := make([]int, 0)
	for k, _ := range m {
		keys = append(keys, k)
	}
	sort.Slice(keys[:], func (i, j int) bool {
		return keys[i] < keys[j]
	})

	for _, key := range keys {
		if m[key] > 0 {
			for j := W - 1; j >= 0; j-- {
				if _, ok := m[key+j]; !ok { return false }
				if m[key+j] - m[key] < 0 { return false }
				m[key+j] -= m[key]
			}
		}
	}

	return true
}
