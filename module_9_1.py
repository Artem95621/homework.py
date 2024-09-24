def apply_all_func(int_list, *function):
    result = {}
    for new_func in function:
            try:
                result[new_func.__name__] = new_func(int_list)
            except Exception as e:
                result[new_func.__name__] = f"Ошибка: {str(e)}"
    return result
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))