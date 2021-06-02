#bubble sort function
def bubble_sort(array):
    #flag variable 
    isSorted = False
    #swap counter
    swaps = 0
    #while array is not sorted execute while loop
    while not isSorted:
        #change isSorted to true
        #if we don't enter the if conditional
        #this will skip for loop and return array
        isSorted = True
        #loop through length of array -1  -swaps
        #if i greater than i + 1 call swap helper func
        #comma assignment to swap index positions
        #flag isSorted back to false
        for i in range(len(array) - 1 - swaps):
            if array[i] > array[i + 1]:
                swap(i, i+1, array)
                isSorted = False
        #increment swaps
        swaps += 1

    return array

#helper func using comma assignment
#could have just put it in bubble sort since it's only 1 line
#but this practices helper functions and I'd do this in JS since it's a little more tedious
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

