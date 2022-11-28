class Solution:
    # O(n + k) time | O(n) space - Need to know how the range of players in advance.
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = 100001
        loss = [-1] * players
        for winner, loser in matches:
            if loss[loser] == -1:
                loss[loser] = 0
            loss[loser] += 1
            
            if loss[winner] == -1:
                loss[winner] = 0
        
        ans = [[], []]
        for i in range(players):
            losses = loss[i]
            if -1 < losses < 2:
                ans[losses].append(i)
        
        return ans
