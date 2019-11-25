"""
Longest Increasing Subsequence problem challenges us to find an increasing
subsequence within a given sequence
eg S= {2,4,3,5,1,7,6,9,8}

lis = {2,3,5,6,8}

"""


def calculate_longest_increasing_subsequence(input_sequence):
  input_sequence_size = len(input_sequence)
  subsequence_length_array = [1] * input_sequence_size
  predecessor_index_array = [-1] * input_sequence_size

  for i in range(1,input_sequence_size):
    for j in range(0, i):
      if int(input_sequence[j]) < int(input_sequence[i]):
        current_value = subsequence_length_array[j]
        next_value = current_value + 1
        max_value = find_max(current_value, next_value)
        if max_value > subsequence_length_array[i]:
          subsequence_length_array[i] = max_value
          predecessor_index_array[i] = j
  return subsequence_length_array[input_sequence_size - 1]


def find_max(value1, value2):
  if value1 < value2:
    return value2
  else:
    return value1


if __name__ == "__main__":
  input_sequence = input().split(" ")
  lis_length = calculate_longest_increasing_subsequence(input_sequence)
  print(lis_length)
