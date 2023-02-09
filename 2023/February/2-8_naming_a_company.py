class Solution:
    # O(n * m) time | O(n * m) space
    # n is the number of strings and m is the length of the longest string.
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        groups = [set() for _ in range(26)]

        for idea in ideas:
            idx = ord(idea[0]) - ord('a')
            groups[idx].add(idea[1:])
        
        for i in range(26):
            for j in range(i, 26):
                common_suffixes = len(groups[i] & groups[j])  # intersection of two sets

                distinct_suffixes_i = len(groups[i]) - common_suffixes
                distinct_suffixes_j = len(groups[j]) - common_suffixes

                ans += 2 * (distinct_suffixes_i * distinct_suffixes_j)
        
        return ans
