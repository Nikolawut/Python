def find_max_product_subsequence(nums):
    max_p = 0
    max_sq = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            product = 1
            for num in nums[i:j]:
                product *= num
            if product > max_p:
                max_p = product
                max_sq = nums[i:j]
    return max_sq, max_p

nums = [1, 2, 2, 2, 4, 4]
subsequence, product = find_max_product_subsequence(nums)
print("Najveća vrijednost:", product, "za sekvencu:", subsequence)