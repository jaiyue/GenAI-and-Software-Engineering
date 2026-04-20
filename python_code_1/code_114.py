def minSubArraySum(nums):
    if not nums:
        raise ValueError("nums must be non-empty")
    current_min = result = nums[0]
    for x in nums[1:]:
        current_min = min(x, current_min + x)
        if current_min < result:
            result = current_min
    return result

This uses the Kadane-style scan adapted to track the minimum running subarray sum (O(n) time, O(1) extra space). Example: minSubArraySum([2,3,4,1,2,4]) == 1 and minSubArraySum([-1,-2,-3]) == -6.

