class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        start = 1
        end = len(skill)-2
        
        sum = skill[0]+skill[len(skill)-1]
        chemistry = skill[0]*skill[len(skill)-1]

        while start < end :
            if sum != skill[start]+skill[end]:
                return -1
            
            chemistry += skill[start]*skill[end]
            start += 1
            end -= 1
        
        return chemistry
            

        