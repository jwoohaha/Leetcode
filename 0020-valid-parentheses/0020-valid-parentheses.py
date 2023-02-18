class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(', '[', '{'}
        close_brackets = {')': '(', ']': '[', '}': '{'}
        stk = []
        # 괄호 추가 및 검증
        for char in s:
            # 여는 괄호면 추가
            if char in open_brackets:
                stk.append(char)

            # 닫는 괄호일 때
            elif char in close_brackets:
                if not stk or close_brackets[char] != stk.pop():
                    return False
        # 다 돌고난 후
        if not stk:
            # stk이 비어 있으면 제대로 짝을 이룸
            return True
        else:
            return 0