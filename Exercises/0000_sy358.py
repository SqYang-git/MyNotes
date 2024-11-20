# 判断是否为正整数平方
def is_square(n):
    return int(n ** 0.5) ** 2 == n and n > 0
# 相对来讲还是不喜欢global一个result.这个解答设置了bool类型的返回值,也方便扔进判断条件


# 定义从0开始搜索的dfs
def dfs(num_str, start):
    # 如果已经到达字符串的末尾，返回True
    if start == len(num_str):
        return True
    # 初始化结果为False
    result = False
    # 遍历所有start后可能的分割列
    for end in range(start + 1, len(num_str) + 1):
        # 取出子字符串
        sub_num = num_str[start:end]
        # 如果子字符串是一个平方数,并且剩余部分也是一个被祝福的ID
        if is_square(int(sub_num)) and dfs(num_str, end):
            # 是故是一个被祝福的ID
            result = True
            break
    return result


a = int(input())
num_str = str(a)
print("Yes" if dfs(num_str, 0) else "No")
