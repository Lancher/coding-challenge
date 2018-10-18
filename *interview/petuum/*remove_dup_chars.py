

def remove_dup_characters(s):
    # init
    n = len(s)
    stack = []

    # iterate the string
    for i in range(n):
        # if stack if empty or character not match
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()

    # concatenate all the characters in the stack
    return ''.join(stack)


print(remove_dup_characters("abbbbcc"))


def remove_dup_characters_2_pointers(s):
    # init
    l = list(s)
    n = len(l)
    stack_n = 0

    # iterate the string
    for i in range(n):
        if stack_n == 0 or l[i] != l[stack_n-1]:
            l[stack_n] = l[i]
            stack_n += 1
        else:
            stack_n -= 1

    # return the stack with prefix length
    return ''.join(l[:stack_n])


print(remove_dup_characters_2_pointers("abbbbcc"))

