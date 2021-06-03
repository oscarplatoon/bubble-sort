def bubble_sort(sequence):

    y=0

    while y < (len(sequence)-1):
    # for i, num in enumerate(sequence):
        if sequence[y]>sequence[y+1]:
            var1= sequence[y]
            var2= sequence[y+1]
            sequence[y] = var2
            sequence[y+1] = var1
            y=0
        else:
            y=y+1
    result = sequence
    print(f"Final result: {result}")
    return result
    # print(f"Swaps: {swaps}")
bubble_sort([4, 3, 5, 0, 1])