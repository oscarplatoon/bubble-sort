sequence = [4, 3, 5, 0, 1]
swaps = 0

# Your Code Here

def bubble_sort(list):
    result = []
    for index range(0, len(list)-1):
        if list[index] > list[index + 1]:
            to_be_removed = list[index + 1]
            result.append(list[index+1])
            # swaps += 1
    return result
            


bubble_sort(sequence)
print(f"Final result: {result}")
print(f"Swaps: {swaps}")
