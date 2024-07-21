def max_num(weights):
    result = 0
    weights = [-float('inf')] + weights
    for i in range(1, len(weights) - 1):
        if weights[i-1] < weights[i] and weights[i] > weights[i+1]:
            result += 1
    return result 


assert max_num([4, 3, 6, 5, 3, 4, 7, 1]) == 3



