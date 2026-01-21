class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in close_to_open.values():      # opening bracket
                stack.append(ch)
            else:                                 # closing bracket
                if not stack:
                    return False
                if stack[-1] != close_to_open[ch]:
                    return False
                stack.pop()

        return not stack
