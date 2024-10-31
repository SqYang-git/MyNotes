n = int(input())
str1 = "".join([str(i + 1) for i in range(n)])


def order_n(str1):
    ans = []
    # 字符串为空时，返回一个空字符串构成的列表
    if len(str1) == 0:
        ans.append("")
        return ans
    if len(str1) == 1:
        ans.append(str1)
        return ans
    # 遍历字符串的每一个字符
    for i in range(len(str1)):
        # 当前字符
        current = str1[i]
        # 剩余字符，排除当前字符
        remain = str1[:i] + str1[i + 1:]
        # 对剩余字符生成全排列，并加上当前字符进行组合
        for _ in order_n(remain):
            ans.append(current + " " + _)
    return ans


ans = order_n(str1)
for i in ans:
    print(i)
