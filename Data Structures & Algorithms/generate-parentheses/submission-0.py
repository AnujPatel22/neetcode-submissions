class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sol = [], []

        def para(openN, closedN):

            if openN == closedN == n:
                res.append(''.join(sol))
                return

            if openN < n:
                sol.append('(')
                para(openN+1, closedN)
                sol.pop()

            if closedN < openN:
                sol.append(')')
                para(openN, closedN+1)

                sol.pop()

        para(0, 0)
        return res