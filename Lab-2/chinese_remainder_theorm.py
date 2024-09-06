def find_min_x(nums, rems):
    x = max(nums)
    while True:
        # Check if remainder of x % nums[j] is rem[j] for all j from 0 to k-1
        for j in range(len(nums)):
            if x % nums[j] != rems[j]:
                break
        # If all remainders matched, we found x
        if j == len(nums) - 1:
            return x
        # Else, try the next number
        x += 1
    return x

nums = list(map(int,input("Enter the list of numbers: ").split()))
rems = list(map(int,input("Enter the list of numbers: ").split()))
print("The number when divided by numbers[i] has the remainder of remainder[i] is ",find_min_x(nums, rems))


