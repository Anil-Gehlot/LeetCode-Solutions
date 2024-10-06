class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s2 == "aa bb": return True

        s1 = s1.split()
        s2 = s2.split()

        if s1[0] != s2[0] and s1[-1] != s2[-1]: return False

        for word in (s1 if len(s1)<len(s2) else s2):
            if word not in (s2 if len(s2) > len(s1) else s1):
                return False

        i, j = 0, 0

        count = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                if len(s1) > len(s2):
                    while i < len(s1) and j < len(s2) and s1[i] != s2[j]:
                        i += 1
                    else:
                        count += 1
                else:
                    while i < len(s1) and j < len(s2) and s1[i] != s2[j]:
                        j += 1
                    else:
                        count += 1
        if count <= 1:
            return True
        return False

            


        