def sum_of_intervals(intervals):
    for i in range(len(intervals)):
        intervals[i] = intervals[i][1] - intervals[i][0]
    print(intervals)
    return sum(intervals)

print(sum_of_intervals([(1, 5), (1, 5)]))