# LEETCODE@ 384. Shuffle an Array
#
#
# Here is my understanding of the correctness of this algorithm. Hope it will be helpful!
#
# Each element has equal probability of being at one of the available positions in the array.
#
# Iteration 1: 1 element , 1 available position.(i=0, j=0) Prob that this element is put in the available posiition is 1/1.
#
# Iteration 2: 2 elemenst, 2 available positions.
# prob that 0th element goes to 1st position (i=0, j=1)
# = Prob that 1st element doesnt remain in its original position * Prob that 0th element gets chosen out of all remaining elements to be in 1st position.
# = 1 - 1/2 * 1/1 = 1/2
#
# prob that 1st element goes to 1st position (i=1, j=1)
# = prob that 1st element remains in its original position * prob that none of the remaining elements get chosen.(as i = j)
# = 1/2 * 1 = 1/2
#
# Iteration 3: 3 elements, 3 available positions.
# prob that 0th element goes to 2nd position (i=0, j=2)
# = prob that 2nd element doesnt remain in its original position * prob that 0th element gets chosen out of all remaining elements to be in 2nd position
# = 1 - 1/3 * 1/2
# = 2/3 * 1/2
# = 1/3
#
# prob that 1st element goes to 2nd position (i=1, j=2)
# = prob that 2nd element doesnt remain in its original position * prob that 1st element gets chosen out of all remaining elements to be in 2nd position
# = 1 - 1/3 * 1/2
# = 2/3 * 1/2
# = 1/3
#
# prob that 2nd element goes to 2nd position (i=2, j=2)
# = prob that 2nd element remains in its original position * prob that none of the remaining elements get chosen.
# = 1/3 * 1 = 1/3
#
# Thus by choosing one element at random between [0, j+1) and swapping with jth element, we generate permutations with equal probability.
#
# We can generalize the above.


