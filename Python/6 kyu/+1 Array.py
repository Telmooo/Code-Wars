def up_array(arr):
    if not arr or any(x<0 or x>=10 for x in arr):
        return
    n = int("".join(str(x) for x in arr))
    n += 1
    return [int(x) for x in str(n)]
