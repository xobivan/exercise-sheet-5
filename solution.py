def theMostExpensiveGift(gifts, customers):
    res = [None]*len(customers)
    sold = [False]*len(gifts)
    for i in range(len(customers)):
        idx = binarySearchClosest(customers[i], gifts)
        while idx >= 0 and sold[idx]:
            idx-=1
        if idx >= 0:
            sold[idx] = True
            res[i] = gifts[idx]
        else:
            res[i] = 0
    return res
            
def binarySearchClosest(target, gifts):
    left = 0
    right = len(gifts) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if gifts[mid] <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans