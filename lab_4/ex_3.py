def sort_mini_puzir(arr):
    sorting_steps = []
    len_arr = len(arr)
    for i in range(len_arr - 1):
        for j in range(len_arr - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        sorting_steps.append(list(arr))
    return sorting_steps

if __name__ == '__main__':
    array = input().split(' ')
    arr = [int(i) for i in array]
    sorting_steps = sort_mini_puzir(arr)
    for steps in sorting_steps:
        print(' '.join(str(i) for i in steps))