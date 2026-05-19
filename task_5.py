def check_values(a, b):
    if a and not b:
        return True
    elif a is None or b is None:
        return None
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


flag = True
while flag:
    flag = False
