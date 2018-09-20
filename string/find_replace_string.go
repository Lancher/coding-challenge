// LEETCODE@ 833. Find And Replace in String
//
// --END--


package string


type Replace struct {
	Idx int
	Src string
	Tar string
}

func findReplaceString(S string, indexes []int, sources []string, targets []string) string {
	s := make([]Replace, 0)
	n := len(indexes)
	for i := 0; i < n; i++ {
		s = append(s, Replace{indexes[i], sources[i], targets[i]})
	}
	sort.Slice(s[:], func (i, j int) bool {
		return s[i].Idx < s[j].Idx
	})

	// from right to left, so the index won't be affect
	for i := n - 1; i >= 0; i-- {
		if S[s[i].Idx:s[i].Idx+len(s[i].Src)] == s[i].Src {
			S = S[:s[i].Idx] + s[i].Tar + S[s[i].Idx+len(s[i].Src):]
		}
	}

	return S
}