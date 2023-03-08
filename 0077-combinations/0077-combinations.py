class Solution(object):
    def combine(self, n, k):
        results = []

        def dfs(case, start, k):
            '''
            case: 만들고 있는 조합
            start: 남은 수 후보의 시작 값
            k: 남은 조합 기회
            '''
            # 조합이 완료되면 결과에 추가
            if k == 0:
                results.append(case[:])
                return

            # 재귀적으로 조합
            for i in range(start, n+1):
                case.append(i)
                dfs(case, i+1, k-1)
                case.pop()

        dfs([], 1, k)
        return results

        