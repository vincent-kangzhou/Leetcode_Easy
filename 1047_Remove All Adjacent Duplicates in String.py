class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        for s in S:
            if stack and s==stack[-1]:
                stack.pop()
                continue
            stack.append(s)
            
        return ''.join(stack
