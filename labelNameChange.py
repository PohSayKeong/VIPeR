allLabels = []
with open('Label.txt') as f:
    for line in f:
        label = line.split()
        allLabels.append(label)
print(allLabels[631])
print(len(allLabels))
for i in range(len(allLabels)):
    file = open(allLabels[i][0] + ".jpeg.txt","w")
    file.write('\n'.join(allLabels[i][1:]))
    file.close() 

