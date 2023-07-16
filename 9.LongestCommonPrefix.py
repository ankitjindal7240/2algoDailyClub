arr = ["flower","flow","flight"]
def longestCommonPrefix(arr):
    n = len(arr)
    if n==0:
        return ""
    if n ==1:
        return arr[0]
    arr.sort()

    min_str = min(len(arr[0]),len(arr[-1]))
    i =0
    while i< min_str and arr[0][i] == arr[-1][i]:
        i = i+1
    return arr[0][:i]
print(longestCommonPrefix(arr))