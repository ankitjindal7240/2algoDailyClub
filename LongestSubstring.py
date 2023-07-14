# Longest Substring Without Repeating Characters
str = "abbcdeffffffffggggghrilkjh"
# sliding window technique

def longestSubstring(str):
    max_len = 0
    left =0
    right =0
    dict = {}
    for i in range(len(str)):
        if str[i] not in dict:
            dict[str[i]] = i
        elif dict[str[i]]>= left:
            if (right - left) > max_len:
                max_len = right - left
            left = dict[str[i]]+1

            dict[str[i]] = i
        else:
            dict[str[i]] = i
        right = right + 1
    if (right - left )> max_len:
        max_len = right - left
    print(max_len)
longestSubstring(str)