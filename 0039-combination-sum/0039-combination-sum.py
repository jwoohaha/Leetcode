class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []  # 합이 target인 집합을 저장하는 리스트
        def dfs(tmp_sum, idx, comb):
            '''
            숫자 조합의 합, 인덱스, 숫자 조합
            '''
            # 합이 목표치를 넘으면 가지치기
            if tmp_sum > target:
                return
            # 합이 목표치와 같으면 결과에 저장
            if tmp_sum == target:
                results.append(comb)
                return

            # idx 포함, 이후 숫자를 재귀적으로 추가
            for i in range(idx, len(candidates)):
                dfs(tmp_sum + candidates[i], i, comb + [candidates[i]])

        dfs(0, 0, [])
        return results