class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        I, J = max(rec1[0],rec2[0]), max(rec1[1],rec2[1])
        K, L = min(rec1[2],rec2[2]), min(rec1[3],rec2[3])
        return True if (max((K-I),0)*max((L-J),0)) > 0 else False