class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        component = {}

        def find(x: str) -> int:
            if x not in component:
                component[x] = x

            if component[x] != x:
                component[x] = find(component[x])
                
            return component[x]
        
        def union(x: str, y: str) -> None:
            x = find(x)
            y = find(y)

            if x < y:
                component[y] = x
            else:
                component[x] = y

        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        ans = ''
        for c in baseStr:
            ans += find(c)
        
        return ans
