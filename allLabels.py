allLabels = []
with open('Label.txt') as f:
    for line in f:
        label = line.split()
        allLabels.append(label)
print(len(allLabels))
noDup = []
for i in range (len(allLabels)):
    for x in range (len(allLabels[i])):
        if allLabels[i][x] not in noDup and x!=0:
            noDup.append(allLabels[i][x])
print(len(noDup))
with open("labels.txt","w+") as l:
    for item in noDup:
        l.write("%s\n" % item)
