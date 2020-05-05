import csv

#reads csv file into list of lists
filename = input("Please input file name/location(ie test.csv)")
with open(filename, 'r') as f:
    reader = csv.reader(f)
    matrix = list(reader)
    voters = len(matrix)-1

#variables
candidates = [0, 0, 0, 0]
test = 0

#round 1
for j in range(1, len(matrix)):
    if int(matrix[j][2]) == 1:
        candidates[0] += 1
    elif int(matrix[j][2]) == 2:
        candidates[1] += 1
    elif int(matrix[j][2]) == 3:
        candidates[2] += 1
    elif int(matrix[j][2]) == 4:
        candidates[3] += 1
    else:
        test += 1
print("Round 1")
print("Truett: "+str(candidates[0]))
print("Katie: "+str(candidates[1]))
print("Preston: "+str(candidates[2]))
print("Sarah: "+str(candidates[3]))
print(str(voters))
print("")

#round 2
maxCount = 0
maxPerson = 0
minCount = 100
minPerson = 0
for i in range(4):
    if candidates[i] < minCount:
        minCount = candidates[i]
        minPerson = i
    if candidates[i] > maxCount:
        maxCount = candidates[i]
        maxPerson = i
if maxCount * 2 < voters:
    for j in range(1, len(matrix)):
        if int(matrix[j][2]) == minPerson:
            if int(matrix[j][3]) == 1:
                candidates[0] += 1
                candidates[minPerson] -= 1
            elif int(matrix[j][3]) == 2:
                candidates[1] += 1
                candidates[minPerson] -= 1
            elif int(matrix[j][3]) == 3:
                candidates[2] += 1
                candidates[minPerson] -= 1
            elif int(matrix[j][3]) == 4:
                candidates[3] += 1
                candidates[minPerson] -= 1
            else:
                test += 1

    print("Round 2")
    print("Truett: "+str(candidates[0]))
    print("Katie: "+str(candidates[1]))
    print("Preston: "+str(candidates[2]))
    print("Sarah: "+str(candidates[3]))
    print(str(voters))
