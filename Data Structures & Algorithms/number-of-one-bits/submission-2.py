class Solution:
    def hammingWeight(self, n: int) -> int:

        # count = 0
        ans = 0
        # m = n
        while n !=0:
            if n % 2 ==1:
                ans += 1
            
            n = n>>1
            
            # print(m)
            # count += 1


        return ans
        