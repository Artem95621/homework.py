first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(n) for n in first_strings if len(n) >= 5]

second_result = [(n1,n2) for n2 in second_strings for n1 in first_strings if len(n2) == len(n1)]

third_result = {n: len(n) for n in second_strings + first_strings if len(n) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)