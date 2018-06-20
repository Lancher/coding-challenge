

# time complexity O(n^2)
class ShellSort:

    def sort(self, nums):
        h = 1
        while h * 3 + 1 < len(nums):
            h = h * 3 + 1

        while h >= 1:
            for i in range(h, len(nums)):
                for j in range(i, h - 1, -h):
                    if nums[j] < nums[j-h]:
                        nums[j], nums[j-h] = nums[j-h], nums[j]
                    else:
                        break
            h /= 3
