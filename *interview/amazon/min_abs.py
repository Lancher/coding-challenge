def minimizeSumOfAbsoluteDifferences(a, b):
    # Step 1: Sort both arrays in non-decreasing order
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    
    # Step 2: Initialize the sum of absolute differences
    sum_of_abs_diff = 0
    
    # Calculate the sum of absolute differences between corresponding elements
    for i in range(len(a_sorted)):
        sum_of_abs_diff += abs(a_sorted[i] - b_sorted[i])
    
    # Return the calculated sum
    return sum_of_abs_diff

# Example usage
a = [1, 4, 10]
b = [2, 20, 3]
assert minimizeSumOfAbsoluteDifferences(a, b) == 12
