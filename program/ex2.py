def character_replacer(duplicates, replacement_char):
    def replace_duplicates(input_string):
        unique_chars = set()
        result = ""

        for char in input_string:
            if char in unique_chars:
                result += replacement_char
            else:
                result += char
                unique_chars.add(char)

        return result

    return replace_duplicates


# Example usage:
replace_duplicates = character_replacer(duplicates=['a', 'b', 'c'], replacement_char='*')

# Input string
input_string = "aabccdeeff"

# Call the internal closure function and display the result
result_string = replace_duplicates(input_string)
print(result_string)
