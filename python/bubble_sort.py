sequence = [4, 3, 5, 0, 1]
swaps = 0

# Your Code Here
x=0
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
# print(f"Swaps: {swaps}")
