def aggregate(*args, **kwargs):
    count_dict = {}
    a = [*args]
    b = [key for key, value in kwargs.items() for _ in range(value)]
    c = a + b
    for item in c:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

