sequence = [4, 3, 5, 0, 1]
swaps = 0


flag =1
while flag == 1:
    prev = 0
    current = 1
    flag = 0
    while current <= (len(sequence)-1):
        hold = sequence[current]
        if sequence[prev] > sequence[current]:
            sequence[current] = sequence[prev]
            sequence[prev] = hold
            swaps += 1
            flag = 1
        prev += 1
        current += 1


print(f"Final result: {sequence}")
print(f"Swaps: {swaps}")
