calls = 0
is_contains=0
string_info=0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string in [string for string in list_to_search]

print(string_info('lemon'))
print(string_info('Motorcycle'))
print(is_contains('UrbaN', ['ban', 'BaNaN', 'UrbaN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)