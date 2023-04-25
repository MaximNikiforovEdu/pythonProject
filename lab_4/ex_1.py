def sort_viborom(arr):
    sorting_steps = []
    len_arr = len(arr)
    for i in range(len_arr - 1):
        j = i
        for index in range(i + 1, len_arr):
            if arr[index] < arr[j]:
                j = index
        arr[i], arr[j] = arr[j], arr[i]
        sorting_steps.append(list(arr))
    return sorting_steps



if __name__ == '__main__':
    array = input().split(' ')
    arr = [int(i) for i in array]
    sorting_steps = sort_viborom(arr)
    for steps in sorting_steps:
        print(' '.join(str(i) for i in steps))