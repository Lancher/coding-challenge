// LEETCODE@ 748. Shortest Completing Word
//
// --END--


package hash

import "strings"

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1


func shortestCompletingWord(licensePlate string, words []string) string {
	// counter the words
	licensePlate = strings.ToLower(licensePlate)
	counter := make([]int, 26)
	for _, ch := range(licensePlate) {
		if 0 <= ch - 'a' && ch - 'a' < 26 {
			counter[ch-'a'] += 1
		}
	}

	// check word one by one
	res, ln := "", MaxInt
	for _, word := range(words) {
		tmp_counter := make([]int, 26)
		copy(tmp_counter, counter)

		// iterate charcters
		for _, ch := range(word) {
			tmp_counter[ch-'a'] -= 1
		}

		// check counter
		isMatched := true
		for _, v := range(tmp_counter) {
			if 0 < v {
				isMatched = false
				break
			}
		}

		// update res if possible
		if isMatched {
			if len(word) < ln {
				res, ln = word, len(word)
			}
		}
	}

	return res
}