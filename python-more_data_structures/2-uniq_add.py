def uniq_add(my_list=[]):
    uniq_set = set()
    sum = 0
    for num in my_list:
        if isinstance(num, int):
            if num not in uniq_set:
                uniq_set.add(num)
                sum += num
    return sum
