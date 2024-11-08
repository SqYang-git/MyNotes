list_input = list(map(str, input().split()))
dict_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1000000}
is_positive = True
if list_input[0] == "negative":
    is_positive = False
    list_input = list_input[1:]
result = 0
buffer = 0
for string in list_input:
    if string == "thousand" or string == "million":
        result += buffer * dict_num[string]
        buffer = 0
        continue
    if string == "hundred":
        buffer = buffer * 100
    else:
        buffer += dict_num[string]

if is_positive:
    print(result + buffer)
else:
    print(-(result + buffer))
