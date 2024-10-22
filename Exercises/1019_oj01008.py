def FormHabbToTzolkin(int_day, month, int_year):
    list_Habb_month = ["pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", "yax", "zac", "ceh", "mac",
                       "kankin", "muan", "pax", "koyab", "cumhu", "uayet"]
    list_Tzolkin = ["imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", "ok", "chuen", "eb",
                    "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"]
    num = int_day + 1 + list_Habb_month.index(month) * 20 + int_year * 365
    Year = num // 260 - 1 if num % 260 == 0 else num // 260
    num = num % 260
    NameOfTheDay = list_Tzolkin[num % 20 - 1]
    date = 13 if num % 13 == 0 else num % 13
    return str(date) + " " + NameOfTheDay + " " + str(Year)


n = int(input())
ans = [f"{n}"]
for i in range(n):
    day, month, year = input().split()
    int_day = int(day[:len(day)-1])
    int_year = int(year)
    ans.append(FormHabbToTzolkin(int_day, month, int_year))
print("\n".join(ans))
