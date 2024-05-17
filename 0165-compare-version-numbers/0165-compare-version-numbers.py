class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # Split the version strings by the dot
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")

        # Get the maximum length of the two lists
        max_length = max(len(revisions1), len(revisions2))

        # Compare each revision number
        for i in range(max_length):
            
            # Get the current revision number or 0 if index is out of bounds
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0

            # Compare the current revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1

        # If all revisions are equal
        return 0