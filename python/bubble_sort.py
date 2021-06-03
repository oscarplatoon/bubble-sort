def bubble_sort(sequence):
  #Variable to keep track of amount of times to swap
  count = 0
  #Nested for loop to grab initial and next item in list
  for i in range(len(sequence)):
    for j in range(len(sequence) - 1):
      #Check if initial item is greater than item next to it
      if sequence[j] > sequence[j + 1]:
        sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
        count += 1
  print(type(sequence))
  return sequence, count



  #return results
#print(f"Final result: {result}")
#print(f"Swaps: {swaps}")
print(bubble_sort([1, 7, 8, 6, 3, 2, 4]))