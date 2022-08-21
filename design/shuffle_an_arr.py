# 384. Shuffle an Array
# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array


    def shuffle(self) -> List[int]:
        aux = list(self.array)
        n = len(self.array)

        for i in range(n):
            remove_idx = random.randrange(len(aux))
            self.array[i] = aux.pop(remove_idx)

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()