str1 = input()
str2 = input()
str1_lower = str1.lower()
str2_lower = str2.lower()
if str1_lower < str2_lower:
    print("-1")
elif str1_lower > str2_lower:
    print("1")
else:
    print("0")
