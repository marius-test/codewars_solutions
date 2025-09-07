def solution_v1(nums):
    if nums is not None:
        nums.sort()
    else:
        nums = []
    
    return nums


def solution_v2(nums):
    if nums is None:
        return []

    return sorted(nums)
