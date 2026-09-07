class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        counts = {}
        max_count = 0
        answer = 0

        for r in range(len(s)):
            c = s[r]

            # if c not in counts:
            #     counts[c] = 1
            # else:
            #     counts[c] += 1

            counts[c] = counts.get(c, 0) + 1
            max_count = max(max_count, counts[c])

            while (r - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1

            answer = max(answer, r - l + 1)

        return answer
        