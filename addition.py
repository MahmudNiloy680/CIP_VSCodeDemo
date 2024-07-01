def sum_nums(nums_list):
    result = sum(nums_list)
    return result

nums = list(map(float, input("Enter numbers separated by space: ").split()))
result = sum_nums(nums)
print(result)