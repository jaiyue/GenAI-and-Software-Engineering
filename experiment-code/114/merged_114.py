def minSubArraySum(nums):
    if not nums:
        raise ValueError("nums must be non-empty")
    current_min = result = nums[0]
    for x in nums[1:]:
        current_min = min(x, current_min + x)
        if current_min < result:
            result = current_min
    return result

