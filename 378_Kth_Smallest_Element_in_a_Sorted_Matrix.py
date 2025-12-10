class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis = []
        for l in matrix:
            lis = lis + l
        lis = sorted(lis)
        return lis[k-1]
# asked to craete a code bette than O(n^2)
# this is the bute force method , whihc is better than n squre i guess
