class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        
        if not img or not img[0]:
            return []

        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                neighbors_sum = 0
                neighbors_count = 0

                for ni in range(max(0, i - 1), min(m, i + 2)):
                    for nj in range(max(0, j - 1), min(n, j + 2)):
                        neighbors_sum += img[ni][nj]
                        neighbors_count += 1

                result[i][j] = neighbors_sum // neighbors_count

        return result