def available(email):
    if email.count('@') != 1:
        return False
    if email.startswith('@') or email.startswith('.'):
        return False
    if email.endswith('@') or email.endswith('.'):
        return False
    if email.rfind('@') > email.rfind('.'):
        return False
    if email[email.rfind('@') + 1] == '.':
        return False
    if email[email.rfind('@') - 1] == '.':
        return False
    return True


while True:
    try:
        email = input()
        if available(email):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
