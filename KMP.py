# KMP
def kmp_match(s_str, p_str):
    s_len, p_len = len(s_str), len(p_str)
    cur = 0
    table = partial_table(p_str)
    while cur <= s_len - p_len:
        for i in range(s_len):
            if s_str[i + cur] != p_str[i]:
                cur += max(i - table[i-1], 1)
                break
            else:
                return True
        return False

def partial_table(p_str):
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, le n(p_str)):
        prefix.add(p_str[:i])
        postfix = {p_str[j:i] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret
print(kmp_match("BBC ABCDAB ABCDABDABDE", "ABCDABD"))

