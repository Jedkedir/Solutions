def swap_case(s):
    res = ''
    for ch in str(s):
        if ch.isalpha() & ch.isupper():
            res = res + ch.lower()
        elif ch.isalpha() & ch.islower():
            res = res + ch.upper()
        else:
            res = res + ch
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)