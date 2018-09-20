// LEETCODE@ 759. Employee Free Time
//
// --END--



package swipe_line

import "sort"

type Pos struct {
	X int
	IsStart int
}

func employeeFreeTime(schedule [][]Interval) []Interval {
	// put all the points into line
	points := make([]Pos, 0)
	for _, row := range(schedule) {
		for _, it := range(row) {
			points = append(points, Pos{it.Start, 0})
			points = append(points, Pos{it.End, 1})
		}
	}

	// sort points by x
	sort.Slice(points, func (i, j int) bool {
		if points[i].X == points[j].X {
			return points[i].IsStart < points[j].IsStart
		} else {
			return points[i].X < points[j].X
		}
	})

	// run swipe line
	res := make([]Interval, 0)
	st := -1
	pre_cnt, cnt := 0, 0
	for _, point := range(points) {
		if point.IsStart == 0 {
			pre_cnt, cnt = cnt, cnt + 1
		} else {
			pre_cnt, cnt = cnt, cnt - 1
		}

		if cnt == 0 && st == -1 {
			st = point.X
		}

		if pre_cnt == 0 && cnt == 1 && st != -1 {
			res = append(res, Interval{st, point.X})
			st = -1
		}
	}
	return res
}
