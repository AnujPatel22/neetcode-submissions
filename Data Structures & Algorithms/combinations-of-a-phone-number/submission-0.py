class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        keypad = {
            "0": " ", "1": "", "2": "abc",
            "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, str_sol):
            if len(str_sol) == len(digits):
                res.append(str_sol)
                return

            cur_d = digits[i]
            letters = keypad[cur_d]

            for char in letters:
                backtrack(i+1, str_sol + char)

        backtrack(0, '')
        return res