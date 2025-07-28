def generate_sorted_list(n):
    if n == 1:
        return [1]
    else:
        return generate_sorted_list(n - 1) + [n]

numbers = generate_sorted_list(12)
print(numbers)