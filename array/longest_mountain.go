// LEETCODE@ 845. Longest Mountain in Array
//
// --END--

package array


func longestMountain(A []int) int {
	n := len(A)
	res := 0
	up, down := 0, 0

	for i := 1; i < n; i++ {
		if 0 < down && A[i-1] < A[i] || A[i-1] == A[i] {
			up = 0
			down = 0
		}

		if A[i-1] < A[i] { up += 1 }
		if A[i-1] > A[i] { down += 1 }
		if 0 < up && 0 < down {
			if res < up + down + 1 { res = up + down + 1 }
		}
	}

	return res
}