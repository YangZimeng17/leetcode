# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        
        for ast in asteroids:
            while res and ast < 0 and res[-1] > 0:
                if res[-1] == -ast: 
                    res.pop()
                    break
                    
                elif res[-1] < -ast:
                    res.pop()
                    continue
                    
                elif res[-1] > -ast:
                    break
            else:
                res.append(ast)
                
        return res