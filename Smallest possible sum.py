def solution(lst):
    min_val, max_val = min(lst), max(lst)
    while min_val != max_val:
        min_idx = lst.index(min_val)
        max_idx = lst.index(max_val)
        lst[max_idx] = lst[max_idx] - lst[min_idx]
        min_val, max_val = min(lst), max(lst)
    return sum(lst)

print(solution([6, 9, 21]))