class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }
        stack = []

        for char in s:
            if char in parentheses_map:
                stack.append(char)
            elif stack and char == parentheses_map[stack[-1]]:
                stack.pop()  
            else:
                return False 

        return not stack


        