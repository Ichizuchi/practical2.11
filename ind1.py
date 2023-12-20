def sum_between_negatives(*args):
    negative_indices = [i for i, arg in enumerate(args) if arg < 0]
    if len(negative_indices) < 2:
        return "Недостаточно отрицательных чисел"
    start_index = negative_indices[0]
    end_index = negative_indices[-1]
    if start_index + 1 >= end_index:
        return "Между первым и последним отрицательными числами нет других чисел"
    return sum(args[start_index + 1:end_index])


result = sum_between_negatives(1, 2, -3, 4, 5, 6, 7, -8)
print(result)
