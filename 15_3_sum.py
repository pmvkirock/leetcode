class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, sol = sorted(nums), []
        #print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1
            while low < high:
                sum3 = nums[i] + nums[low] + nums[high]
                if sum3 == 0:
                    sol.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif sum3 > 0:
                    high -= 1
                else:
                    low += 1
                
        return sol