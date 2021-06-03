from math import nan


sequence = [4, 3, 5, 0, 1]


def bubble_sort(array):
    swaps = 0
    previous = nan
    for i, num in enumerate(array):
        if i == 0:
            previous = num
            continue
        elif num < previous:
            smaller_num = array.pop(i)
            if (i-2) < 0:
                array.insert((i-1), smaller_num)
                swaps += 1
                previous = num
                bubble_sort(array)
            else:
                array.insert((i-2), smaller_num)
                swaps += 1
                previous = num
                bubble_sort(array)
        elif num > previous:
            previous = num
            continue

    return(array)

print(bubble_sort(sequence))