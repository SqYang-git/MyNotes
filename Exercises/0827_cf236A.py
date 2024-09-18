username = input()
distinct_characters = len(set(username))
if distinct_characters % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
