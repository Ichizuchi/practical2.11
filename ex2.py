def character_replacer(duplicates, replacement_char):

    def replace_duplicat(inputstring):
        unique_chars = set()
        result = ""

        for char in inputstring:
            if char in unique_chars:
                result += replacement_char
            else:
                result += char
                unique_chars.add(char)

        return result

    return replace_duplicat


# Example usage:
replace_duplicates = character_replacer(duplicates=['a', 'b', 'c'], replacement_char='*')

# Input string
input_string = "aabccdeeff"

# Вызов внутренней функции закрытия и вывод результата
result_string = replace_duplicates(input_string)
print(result_string)
