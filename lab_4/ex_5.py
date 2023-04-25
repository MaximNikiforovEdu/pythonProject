def h_sort_vstavkami(arr, h):
    sorting_steps = []
    len_arr = len(arr)
    for i in range(h, len_arr):
        elem = arr[i]
        index = i
        while(index >= h and elem < arr[index - h]):
            arr[index] = arr[index - h]
            index -= h
        arr[index] = elem
        sorting_steps.append(list(arr))
    return sorting_steps

if __name__ == '__main__':
    h = int(input())
    array = input().split(' ')
    arr = [int(i) for i in array]
    sorting_steps = h_sort_vstavkami(arr, h)
    for steps in sorting_steps:
        print(' '.join(str(i) for i in steps))