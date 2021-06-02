sequence = [4, 3, 5, 0, 1]

def bubble_sort(list):
    swaps = 0
    result_list = []
    length = len(list)
    
    for i in range(length-1):
        for j in range(0,length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swaps += 1

    result_list = [list, swaps]
    return(result_list, swaps)
result = bubble_sort(sequence)
swaps = result[1]
print(f"Final result: {result}")
print(f"Swaps: {swaps}")
