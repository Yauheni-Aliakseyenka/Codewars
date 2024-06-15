'''
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

n being the length of the string array, if n = 0 or k > n or k <= 0 return ""
(return Nothing in Elm, "nothing" in Erlang).

Note
consecutive strings : follow one after another without an interruption
'''


def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    if k == 1:
        return max(strarr, key=len)
    new_arr = []
    for i in range(len(strarr) - k + 1):
        elem = ''
        for j in range(i, i + k):
            elem += strarr[j]
        new_arr.append(elem)
    return max(new_arr, key=len)


def longest_consec1(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""


def longest_consec2(strarr, k):
    result = ""
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result
