class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in brackets:
                top_element= stack.pop() if stack else'#'
                if brackets [char]!= top_element:
                    return False
            else:
                stack.append(char)
        return not stack
result = Solution()
s= "()"
print(result.isValid(s))