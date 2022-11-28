wireOutput = []
file = open("transOutput.txt", "r")
for line in file:
    wireOutput.append([])
    for c in line:
        if c == "\n":
            pass
        elif c == " ":
            wireOutput[-1].append(-1)
        else:
            wireOutput[-1].append(int(c))

m, n = len(wireOutput), len(wireOutput[0])

# for t in range(100):
#     print(wireOutput[t][1], end="")
# print()
# for t in range(100):
#     print(wireOutput[t][376], end="")

for t in range(m):
    if wireOutput[t][1608] == 1:
        print(wireOutput[t][1608], end="")
print()
for t in range(m):
    if wireOutput[t][1608] == 1:
        print(wireOutput[t][869], end="")
print()
for t in range(m):
    if wireOutput[t][1608] == 1:
        print(wireOutput[t][349], end="")
