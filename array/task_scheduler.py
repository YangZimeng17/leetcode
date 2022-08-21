# 621. Task Scheduler
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        max_freq_ele_count = 0                
        i = 0
        
        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_ele_count = max_freq_ele_count + 1
            i = i + 1
            
        ans = (max_freq - 1) * (n+1) + max_freq_ele_count
        
        return max(ans, len(tasks))