class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def pal(i,sol):
            if i >= len(s):
                res.append(sol.copy())
                return

            for j in range(i , len(s)):
                if self.isPali(s, i, j):
                    sol.append(s[i:j+1])
                    pal(j+1, sol)

                    sol.pop()


        pal(0,[])
        return res

    def isPali(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1 , r-1
        return True
