sequence = [19, 13, 6, 2, 18, 8]

def bubble_sort(sequence):
    swapped = True
    swaps = 0
    
    while(swapped):
        swapped = False
        for i in range(len(sequence) - swaps - 1):
            if sequence[i] > sequence[i + 1]:
                #swapped
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                swapped = True
        
        swaps += 1   
        
bubble_sort(sequence)
print(sequence)
