
def bubble_sort(unsorted_list):
    sorted_list = unsorted_list.copy()
    number_elements = len(sorted_list)
    
    for first_elem_to_be_sorted in range(number_elements-1):

        for current_position in range(0, number_elements - first_elem_to_be_sorted - 1 ):
            next_position = current_position + 1
            if sorted_list[current_position] > sorted_list[next_position]:
               sorted_list[current_position], sorted_list[next_position] = sorted_list[next_position], sorted_list[current_position]

    return sorted_list


