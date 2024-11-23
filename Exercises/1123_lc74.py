class Solution:
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    list = [item for sublist in matrix for item in sublist]
    return target in list