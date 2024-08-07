def move_zeroes(nums):
    """
    Function to move all zeroes in the array `nums` to the end while maintaining the order of non-zero elements.

    :param nums: List[int] - The input array of integers.
    :return: None - The function modifies the input array in place.
    """
    last_non_zero_found_at = 0  # Pointer for the position of the next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

# Example usage:
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print("Array after moving zeroes:", nums)
