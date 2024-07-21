
def match_strings(texts, pats):
    result = []

    for text, pat in zip(texts, pats):
        if regex(text, pat):
            result.append('YES')
        else:
            result.append('NO')
    
    return result
    

def regex(text, pat):
    m, n = len(text), len(pat)
    dp = [[False for j in range(n + 1)] for i in range(m + 1)]

    dp[0][0] = True
    for j in range(n):
        if pat[j] == '*':
            dp[0][j+1] = dp[0][j]
    
    for i in range(m):
        for j in range(n):
            if pat[j] == '*':
                dp[i+1][j+1] = dp[i+1][j] or dp[i][j] or dp[i][j+1]
            elif text[i] == pat[j]:
                dp[i+1][j+1] = dp[i][j]

    return dp[m][n]



assert match_strings(["code", "coder"], ["co*d", "co*er"]) == ['NO', 'YES'] 
assert match_strings(["hackerrank", "hackerrnak"], ["hac*rank", "hac*rnak"]) == ['YES', 'YES'] 



