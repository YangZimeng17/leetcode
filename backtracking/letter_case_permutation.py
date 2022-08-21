# 784. Letter Case Permutation
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [s]
        
        for i, c in enumerate(s):
            if c.isalpha():
                for j in range(len(res)):
                    ans = list(res[j])
                    ans[i] =ans[i].swapcase()
                    res.append(''.join(ans))
        return res