def sort_vstavkami(arr):
    sorting_steps = []
    len_arr = len(arr)
    for i in range(1, len_arr):
        elem = arr[i]
        index = i
        while index > 0 and elem < arr[index - 1]:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = elem
        sorting_steps.append(list(arr))
    return sorting_steps

if __name__ == '__main__':
    array = input().split(' ')
    arr = [int(i) for i in array]
    sorting_steps = sort_vstavkami(arr)
    for steps in sorting_steps:
        print(' '.join(str(i) for i in steps))