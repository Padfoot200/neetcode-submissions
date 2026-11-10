class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_element=nums[0]
        count_major=0
        for x in nums:
            if(x==maj_element):
                count_major+=1
            else:
                count_major-=1
            if(count_major==0):
                maj_element= x
                count_major+=1
        return maj_element