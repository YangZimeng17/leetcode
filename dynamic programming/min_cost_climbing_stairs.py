# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,*15*,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        
        currant=0
        mem0=cost[0]
        
        if n >= 2:
            mem1=cost[1]
        
        for i in range(2, n):
            currant=cost[i] + min(mem0,mem1)
            mem0=mem1
            mem1=currant
            
        return min(mem0,mem1)