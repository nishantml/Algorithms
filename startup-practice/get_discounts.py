def get_discounts(nums, discount):
    discount = discount / 100
    lst = []
    for i in nums:
        lst.append(i * discount)

    return lst


print(get_discounts([10, 20, 40, 80], 75))
