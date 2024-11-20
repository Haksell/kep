def filter_list(lst, flag):
    if flag != 0:
        flag = 1
    return [n for n in lst if (n ^ flag) & 1]
