class Solution:
    def numDecodings(self, s: str) -> int:

        def _decode(s, i, memo):

            if i in memo:
                return memo[i]

            if i==len(s):
                return 1

            if s[i]=="0":
                return 0

            one = _decode(s, i+1, memo)
            two = 0

            if i+1 < len(s) and int (s[i:i+2]) <= 26:
                two = _decode(s, i+2, memo)

            memo[i] = one + two

            return memo[i]

        return _decode(s, 0, {})
        