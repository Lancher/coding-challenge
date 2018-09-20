// LEETCODE@ 738. Monotone Increasing Digits
//
// -- END--


package array


import "strconv"

func monotoneIncreasingDigits(N int) int {
	// convert to string
	str := strconv.Itoa(N)
	s := strings.Split(str, "")

	// from left to right find the first decreasing point.
	n := len(s)
	i := 0
	for i < n - 1 {
		if s[i][0] > s[i+1][0] { break }
		i += 1
	}
	if i == n - 1 { return N }

	// go from right to left
	try_decrease := false
	for 0 <= i {
		if try_decrease {
			if i == 0 || s[i-1][0] <= s[i][0] - 1 {
				s[i] = string(rune(s[i][0] - 1))
				for j := i + 1; j < n; j++ { s[j] = "9"}
				break
			}
			i -= 1
			continue
		}
		if s[i][0] > s[i+1][0] {
			try_decrease = true
		} else {
			i -= 1
		}
	}
	fmt.Println(s)

	res, _ := strconv.Atoi(strings.Join(s, ""))
	return res
}