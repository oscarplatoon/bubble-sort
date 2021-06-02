def bubble_sort(list):
    swaps = 0
    input_list = list
    result_list = []
    length = len(input_list)
    
    #This i value tracks the "completely ordered to the left" index
    for i in range(length-1):

        for j in range(0,length-i-1):

            #If term to the right of j is smaller, invert the one to the other
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

                swaps += 1
        
    result_list = input_list, swaps
    return(result_list)
