class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1

        return max_depth
##  The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )
