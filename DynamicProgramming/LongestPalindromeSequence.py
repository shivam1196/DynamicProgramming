def longest_palindrome_subsequence(input_sequence):
    input_length = len(input_sequence)
    if input_length == 0:
        return ""
    palindrome_string = input_sequence[0]
    palindrome_length = 1

    for i in range(input_length):
        left_index = i - 1
        right_index = i + 1
        interm_palindrome = input_sequence[i]
        interm_length = 1
        while left_index < 0 and right_index < input_length:
            if input_sequence[i] == input_sequence[right_index]:
                interm_length += 1
                interm_palindrome = interm_palindrome + input_sequence[right_index]
                right_index += 1
                if interm_length > palindrome_length:
                    palindrome_length = interm_length
                    palindrome_string = interm_palindrome
            else:
              left_index +=1
              break
        current_difference = 1
        while left_index >= 0 and right_index < input_length:
            while input_sequence[i] == input_sequence[right_index] and right_index-i ==current_difference:
              right_index+=1
              interm_length +=1
              current_difference +=1
              interm_palindrome = interm_palindrome + input_sequence[right_index-1]
              if interm_length > palindrome_length:
                palindrome_length = interm_length
                palindrome_string = interm_palindrome
              if right_index >=input_length-1:
                break
            if right_index <input_length and input_sequence[left_index] == input_sequence[right_index] :
                interm_length += 2
                interm_palindrome = input_sequence[left_index] + interm_palindrome + input_sequence[right_index]
                left_index -= 1
                right_index += 1
                if interm_length > palindrome_length:
                    palindrome_length = interm_length
                    palindrome_string = interm_palindrome
            else:
                break
    return palindrome_string


if __name__ == "__main__":
    text_sequence = input()
    palindrome_string = longest_palindrome_subsequence(text_sequence)
    print(palindrome_string)
