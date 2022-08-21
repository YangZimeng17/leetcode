# 815. Bus Routes
# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        to_routes = collections.defaultdict(set)
        
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
                
        bfs = [(source, 0)]
        seen = set([source])
        
        for stop, bus in bfs:
            if stop == target: 
                return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  
        return -1