class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        orginal_arr_len = len(nums)
        res_arr=[]
        total_removed=0
        k=0
        for i in range(orginal_arr_len):
            current_index=i
            current_val=nums[current_index]
            if current_val!=val:
                nums[k]=nums[i]
                k+=1
            else:
                total_removed+=1
        # res_arr.extend(['_']*total_removed)
        # print("Now the arrays are", nums, res_arr)
        # for i in range(orginal_arr_len):
        #     nums[i]=res_arr[i]

        return k