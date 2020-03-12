arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def media(arr, init, final):
    i = (init - 1)
    pivot = arr[final]

    for j in range(init, final):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[final] = arr[final], arr[i + 1]
    return (i + 1)


def quicksort(arr, min, max):
    if min >= max:
        return

    pivo = media(arr, min, max)
    quicksort(arr, min, pivo - 1)
    quicksort(arr, pivo + 1, max)


n = len(arr)
quicksort(arr, 0, n - 1)

print("Lista ordenada:")
for i in range(n):
    print("%d" % arr[i])