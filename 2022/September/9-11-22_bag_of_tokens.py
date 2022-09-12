class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        score = 0
        i = 0
        j = len(tokens) - 1

        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0 and i != j:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break

        return score