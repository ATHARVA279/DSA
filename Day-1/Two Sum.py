def two_sum(nums, target):
    """
    Function to find two indices in the array `nums` such that their values add up to `target`.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum.
    :return: List[int] - The indices of the two numbers that add up to the target.
    """
    num_map = {}  # Dictionary to store the complement and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Indices of the two numbers are:", two_sum(nums, target))
