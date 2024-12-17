n = int(input())
for _ in range(n):
    coins = {chr(ord('A') + i): "unknown" for i in range(12)}
    for _ in range(3):
        left, right, result = input().split()
        if result == "even":
            for coin in left + right:
                coins[coin] = "even"
        elif result == "up":
            for coin in left:
                if coins[coin] == "unknown":
                    coins[coin] = "heavy"
                elif coins[coin] == "light":
                    coins[coin] = "even"
            for coin in right:
                if coins[coin] == "unknown":
                    coins[coin] = "light"
                elif coins[coin] == "heavy":
                    coins[coin] = "even"
        elif result == "down":
            for coin in left:
                if coins[coin] == "unknown":
                    coins[coin] = "light"
                elif coins[coin] == "heavy":
                    coins[coin] = "even"
            for coin in right:
                if coins[coin] == "unknown":
                    coins[coin] = "heavy"
                elif coins[coin] == "light":
                    coins[coin] = "even"
    for coin, status in coins.items():
        if status in ["heavy", "light"]:
            print(f"{coin} is the counterfeit coin and it is {status}.")
            break
