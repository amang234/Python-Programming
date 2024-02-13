# Find Maximum XOR Pair in an Array
def find_maximum_xor_pair(nums):
    max_xor = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            xor_result = nums[i] ^ nums[j]
            max_xor = max(max_xor, xor_result)
    return max_xor

nums = [3, 10, 5, 25, 2, 8]
print("Maximum XOR pair:", find_maximum_xor_pair(nums))
