import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return cleaned_text == cleaned_text[::-1]
        