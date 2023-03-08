class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        case = []

        def dfs(elements):
            # 남은 원소가 없으면 종료
            if len(elements) == 0:
                # 참조가 아닌 값을 추가해야 하므로 복사
                results.append(case[:])

            # 순열 생성울 위한 재귀 호출
            for num in elements:
                # elements를 건들지 않도록 복사
                candidates = elements[:]
                candidates.remove(num)

                case.append(num)
                dfs(candidates)
                case.pop()

        dfs(nums)
        return results
