input_file = "./part1_input.txt"

with open(input_file,'r') as file:
    rotations = file.readlines()

for i in range(len(rotations)):
    
    if i < len(rotations)-1:
        rotations[i] = rotations[i][:-1]
    

# print(rotations)
curr = 50
count = 0

for r in rotations:
    d, s = r[0], int(r[1:])

    if d == 'L':
        curr = (curr - s + 100) % 100
    else:
        curr = (curr + s) % 100

    if curr == 0:
        count += 1

print(count)