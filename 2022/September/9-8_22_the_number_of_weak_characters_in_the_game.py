class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        ans = 0
        max_def = 0
        for _, _def in properties:
            if max_def > _def:
                ans += 1
            max_def = max(max_def, _def)

        return ans