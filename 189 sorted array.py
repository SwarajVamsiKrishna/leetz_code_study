class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse( A + B )  = reverse(A) + reverse(B)
        n = len(nums)

        #  on  a   5 elemets array , if we rotate 6 times , then it will be 6-5 = 1 time , subtraction is equal to modulo for big numbers 
        k = k % n

        # this si two pointer , shrinking to gether
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)      # step 1
        reverse(0, k - 1)      # step 2
        reverse(k, n - 1)      # step 3        

            
