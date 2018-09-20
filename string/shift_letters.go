// LEETCODE@ 848. Shifting Letters
//
// --END--


package string



func shiftingLetters(S string, shifts []int) string {
	res := ""
	n := len(S)

	cnt := 0
	for i := n - 1; i >= 0; i-- {
		res = string((int(S[i]) - int('a') + shifts[i] + cnt) % 26 + int('a')) + res
		cnt += shifts[i]
	}
	return res
}
