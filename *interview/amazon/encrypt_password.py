
def encrypt_password(password):
    result = []
    single = ''
    chrs = [0] * 26
    for ch in password:
        chrs[ord(ch)-ord('a')] += 1

    for i in range(26):
        if chrs[i] % 2:
            single = chr(ord('a') + i)
        result.append(chr(ord('a') + i) * (chrs[i] // 2))

    result = result + [single] + result[::-1]
    return ''.join(result)


assert encrypt_password('babab') == 'abbba'
assert encrypt_password('yxxy') == 'xyyx'
    