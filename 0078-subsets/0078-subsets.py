class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # 비트 연산으로 부분집합 구하기
        for i in range(1<<len(nums)):
            subset = []
            for j in range(len(nums)):
                if i & (1<<j):
                    subset.append(nums[j])
            result.append(subset)

        return result
        