def maxi_contigous_prod_array(input_list):
    local_minima = 1
    local_maxima = 1
    global_maxima = 0
    if len(input_list) == 1:
        return input_list[0]
    for i in input_list:
        temp_minima = local_minima * i
        temp_maxima = local_maxima * i

        local_minima = find_min(temp_minima, temp_maxima, i)
        local_maxima = find_max(temp_minima, temp_maxima, i)

        if local_maxima > global_maxima:
            global_maxima = local_maxima

    return global_maxima


def find_min(value1, value2, value3):
    if value1 <= value2 and value1 <= value3:
        return value1
    elif value2 <= value1 and value2 <= value3:
        return value2
    else:
        return value3


def find_max(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    elif value2 >= value1 and value2 >= value3:
        return value2
    else:
        return value3


if __name__ == "__main__":
    input_list = [2,3,-2,4]
    prod = maxi_contigous_prod_array(input_list)
    print(prod)
