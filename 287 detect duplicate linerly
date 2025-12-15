class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # floys cycle detection
        # detect cycle
        slow = nums[0]
        fast = nums[0]

        # find the cylce existys or not 
        steps = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            steps += 1
            if slow == fast:
                break
            if steps > len(nums):
                return -1  # invalid input

        # come to start postion to find where the duplicate exists
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
     
