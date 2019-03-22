
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        lefty = '([{'
        righty = ')]}'
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if len(stack) == 0:
                    return False
                if righty.index(c) != lefty.index(stack.pop()):
                    return False
        return len(stack) == 0

    def isValid2(self, s: 'str') -> 'bool':
        if len(s) %2 != 0:
            return False
        lb = {'(':')','[':']','{':'}'}
        stack = []

        for x in s:
            if x in lb:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if lb[top] != x:
                    return False
        return len(stack) == 0

    def isValid3(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
if __name__ == '__main__':
    s = Solution()
    A = "{{{{}}}))"
    print(s.isValid(A))