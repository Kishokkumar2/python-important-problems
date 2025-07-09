def three_sum_unique(nums):
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Ensure all three numbers are different in value
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print("Unique value triplets that sum to 0:", three_sum_unique(nums))
