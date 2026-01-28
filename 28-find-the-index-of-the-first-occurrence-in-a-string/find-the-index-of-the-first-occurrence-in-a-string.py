class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, by problem convention usually return 0
        # (LeetCode does not give this case here, but it's safe.)
        if needle == "":
            return 0

        n, m = len(haystack), len(needle)

        # Brute-force search: try all starting positions where needle can fit
        for i in range(n - m + 1):
            # Check if substring from i of length m matches needle
            if haystack[i:i + m] == needle:
                return i

        # If no match found
        return -1
