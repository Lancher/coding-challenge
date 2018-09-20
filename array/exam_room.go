// LEETCODE@ 855. Exam Room
//
// --END--


package array

import "fmt"

type ExamRoom struct {
	Seats []int
	N int
}


func Constructor(N int) ExamRoom {
	er := ExamRoom{make([]int, 0), N}
	return er
}


func (this *ExamRoom) Seat() int {
	fmt.Println(this.Seats)

	// no one inside
	if len(this.Seats) == 0 {
		this.Seats = append(this.Seats, 0)
		return 0
	}

	// check the first and last section
	max := -1
	if this.Seats[0] < this.N - 1 - this.Seats[len(this.Seats)-1] {
		max = this.N - 1 - this.Seats[len(this.Seats)-1]
	} else {
		max = this.Seats[0]
	}

	// check the gaps
	for i := 0; i < len(this.Seats) - 1; i++ {
		if max < (this.Seats[i+1] - this.Seats[i]) / 2 {
			max = (this.Seats[i+1] - this.Seats[i]) / 2
		}
	}

	// put at 0
	if max == this.Seats[0] {
		this.Seats = append([]int{0}, this.Seats...)
		return 0
	}

	// put between gaps
	for i := 0; i < len(this.Seats) - 1; i++ {
		if max == (this.Seats[i+1] - this.Seats[i]) / 2 {
			pos := this.Seats[i] + max
			newSeats := append([]int{pos}, this.Seats[i+1:]...)
			this.Seats = append(this.Seats[:i+1], newSeats...)
			return pos
		}
	}

	// put at last
	this.Seats = append(this.Seats, this.N - 1)
	return this.N - 1
}


func (this *ExamRoom) Leave(p int)  {
	fmt.Println(this.Seats)

	for i := 0; i < len(this.Seats); i ++ {
		if p == this.Seats[i] {
			this.Seats = append(this.Seats[:i], this.Seats[i+1:]...)
		}
	}
}
