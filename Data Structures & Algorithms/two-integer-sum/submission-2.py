class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            if sum == target:
                return [l,r]
            elif sum< target:
                l+=1
            elif sum > target:
                r-=1
            else:
                return [-1]