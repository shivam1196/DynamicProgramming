def max_contigous_sub_array(num_list):
    max_sum = 0
    max_sum_so_far = 0
    current_sum = 0
    maximum_smallest_number = num_list[0]

    for i in range(len(num_list)):
        current_sum = current_sum + num_list[i]
        if current_sum > 0:
            max_sum = current_sum
            if max_sum > max_sum_so_far:
                max_sum_so_far = max_sum
        elif current_sum <=0:
            current_sum = 0
            if num_list[i] >= maximum_smallest_number:
                maximum_smallest_number = num_list[i]
    if max_sum_so_far == 0:
        max_sum_so_far = maximum_smallest_number


    return max_sum_so_far


if __name__ == "__main__":
    array_list = [-1,0]
    max_sub_array_sum = max_contigous_sub_array(array_list)
    print(max_sub_array_sum)
