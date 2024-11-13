def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    else:
        sums = [0] * n
        for i in range(len(customers)):
            k = i % n
            sums[sums.index(min(sums))] += customers[i]
    return max(sums)



print(queue_time([2, 3, 10], 2))