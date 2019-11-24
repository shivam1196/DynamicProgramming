"""
Approixmate String matching problem

The aim is to find the minimum number of operations required to match a pattern p with a text t.

The solution is provided with the help of dynamic programming technique.

At any given point of time the operation cost will be minimum of the following three operation.

Min =  D[i-1,j-1] if p[j] == t[i], else D[i-1,j-1]+1
       D[i-1,j] + 1 (Insertion cost)
       D[i,j-1] + 1 (Deletion Cost)
"""


def calculate_distance(text, pattern):
    global look_up_table
    text_size = len(text)
    pattern_size = len(pattern)

    text_storage_array = [""]
    pattern_storage_array = [""]

    for i in range(len(text)):
        text_storage_array.append(text[i])
    for j in range(len(pattern)):
        pattern_storage_array.append(pattern[j])

    for i in range(len(text) + 1):
        look_up_table[0][i] = i
        look_up_table[i][0] = i

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if text_storage_array[j] == pattern_storage_array[i]:
                substitute_operation = look_up_table[i-1][j-1]
            else:
                substitute_operation = look_up_table[i-1][j-1] + 1

            insert_operation = look_up_table[i - 1][j] + 1
            delete_operation = look_up_table[i][j - 1] + 1
            look_up_table[i][j] = find_min(substitute_operation, insert_operation, delete_operation)

    return look_up_table[text_size][pattern_size]

def print_lookup_table():
    global look_up_table

    for i in look_up_table:
        print(i)


def find_min(value1, value2, value3):
    if value1 <= value2 and value1 <= value3:
        return value1
    elif value2 <= value1 and value2 <= value3:
        return value2
    else:
        return value3


if __name__ == "__main__":
    text_input = input()
    pattern_input = input()
    rows = len(text_input) + 1
    cols = len(pattern_input) + 1
    global look_up_table
    look_up_table = []
    for i in range(0, rows):
        look_up_table.append([])
    for i in range(0, rows):
        for j in range(0, cols):
            look_up_table[i].append(j)
            look_up_table[i][j] = 0
    number_of_steps=calculate_distance(text_input, pattern_input)
    print_lookup_table()
    print("Total Number of Steps are: ",number_of_steps)
