def maxProduct(self, nums: List[int]) -> int:
    product = maxproduct = nums[0]
    if product < 0:
        stack = [product]
    else:
        stack = []
    for i in range(1, len(nums)):
        if nums[i] > 0:
            if product: 
                product *= nums[i]
            else:
                product = nums[i]
        elif nums[i] < 0:
            if stack:
                product = product * stack.pop() * nums[i]
            else:
                maxproduct = max(maxproduct, product)
                if product:
                    stack.append(product*nums[i])
                else:
                    stack.append(nums[i])
                product = 0
        else:
            maxproduct = max(maxproduct, product)
            stack = []
            product = 0
    return max(maxproduct, product)