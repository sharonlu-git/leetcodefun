class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Take product of entire array
        # Then divide by nums[index] to get new value

        if len(nums) == 2:
            return [nums[1], nums[0]]
        containsZero = False
        prodNums = 1
        for num in nums:
            if num != 0 or containsZero:
                prodNums *= num
            else:
                containsZero = True
        newList = []
        if containsZero == True:
            for num in nums:
                if num == 0:
                    newList.append(prodNums)
                else:
                    newList.append(0)
        else:
            for num in nums:
                newList.append(int(prodNums/num))
        return newList
        
