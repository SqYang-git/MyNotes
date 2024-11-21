# 数学思维,换为二进制,乘2即末尾加一个0,加1即末尾0变为1(为了步数最少)
binary = bin(int(input()))
l = [int(i) for i in binary[2:]]
print(sum(l) + len(l) - 2)
