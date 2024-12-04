stack = []
stack1 = []
while True:
    try:
        command = input().split()
        if command[0] == "push":
            weight = int(command[1])
            stack.append(weight)
            if stack1 == [] or stack1[-1] >= weight:
                stack1.append(weight)
        elif command[0] == "pop":
            if stack:
                front = stack.pop()
                if front == stack1[-1]:
                    stack1.pop()
        elif command[0] == "min":
            if stack1:
                print(stack1[-1])
    except EOFError:
        break
