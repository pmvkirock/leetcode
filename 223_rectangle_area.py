class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        I, J, K, L = max(A,E), max(B,F), min(C,G), min(D,H)
        return ((C-A)*(D-B))+((G-E)*(H-F))-(max((K-I),0)*max((L-J),0))