def sort_shella(arr, h):
    sorting_steps = []
    len_arr = len(arr)
    for h_elem in h:
        for i in range(h_elem, len_arr):
            elem = arr[i]
            index = i
            while(index >= h_elem and elem < arr[index - h_elem]):
                arr[index] = arr[index - h_elem]
                index -= h_elem
            arr[index] = elem
        sorting_steps.append(list(arr))
    return sorting_steps

if __name__ == '__main__':
    h = [int(i) for i in input().split(' ')]
    arr = input().split(' ')
    arr = [int(i) for i in arr]
    sorting_steps = sort_shella(arr, h)
    for steps in sorting_steps:
        print(' '.join(str(i) for i in steps))