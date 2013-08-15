def msort(lst):
    if len(lst) <= 1: return lst
    m = (len(lst) / 2)
    l = msort(lst[:m])
    r = msort(lst[m:])
    return merge(l, r)

def merge(left, right):
    res = []
    i, j = 0, 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res



print msort([])
print msort([1])
print msort([2,1])
print msort([5,12,1,9,2321,2,23,123,1,4,5,6,99])
