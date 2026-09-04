class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early stop
        if len(s) != len(t):
            return False

        count = {}
        for idx in range(len(s)):
            if s[idx] not in count:
                count[s[idx]] = 1
            else:
                count[s[idx]] += 1

            if t[idx] not in count:
                count[t[idx]] = -1
            else:
                count[t[idx]] -= 1

        # print(count)

        return not any(v != 0 for v in count.values())