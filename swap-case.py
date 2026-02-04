
def swap_case(s):
    char = []
    for c in s :
        if c.isupper():
            char.append(c.lower())
        elif c.islower():
            char.append(c.upper())
        else:
            char.append(c)
    
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)