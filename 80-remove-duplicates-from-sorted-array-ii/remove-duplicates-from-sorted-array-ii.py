class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1, index2, count, k = 0, 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index2]:   
                index2 = i     
                count = min(count+1, 2)
                nums[index1:index1+count] = [nums[i-1]] * count
                index1 += count
                k += count                
                count = 0
            else:
                count += 1
        
        if count == 0:
            if index2 == len(nums)-1:
                nums[index1] = nums[-1]
            index1 += 1
        else:
            nums[index1: index1+2] = [nums[-1]] * 2
            index1 += 2
        return index1
                
                
        