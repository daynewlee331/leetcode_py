def rob(nums):
    if len(nums) <= 0:
        return 0
    if len(nums) == 1: 
        return nums[0]
    arr = [0] * len(nums)
    arr[0] = nums[0]
    arr[1] = max(nums[0], nums[1]);
    for i in range(2, len(nums)):
        arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
    return arr[len(nums) - 1]


l = [0] * 5
l.append(4)
l.append(10)
l.append(3)
l.append(1)
l.append(5)
print rob(l)
