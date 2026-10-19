class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}
        ways[1] = 1
        ways[2] = 2

        # ways[3] = (step1+2) + (step2+1)
        # ways[4] = (step2+2) + (step3+1)
        # fibonacci

        i = 1
        first = 0
        second = 1
        while i < n:
            # print(i, first, second)
            new = first + second
            first = second
            second = new
            i+=1
        
        return first+second


        