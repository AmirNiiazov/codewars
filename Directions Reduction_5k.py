def dir_reduc(arr):
    pairs = {'WEST': 'EAST', 'EAST': 'WEST', 'NORTH': 'SOUTH', 'SOUTH': 'NORTH'}
    for i in arr[1:]:
        if i == pairs[arr[arr.index(i)-1]]:
            arr.remove(i)
            arr.remove(arr[arr.index(i)-1])


    return arr

print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
