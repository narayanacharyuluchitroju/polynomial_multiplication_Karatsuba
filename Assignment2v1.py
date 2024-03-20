############
# Project : Karatsuba Algorithm for Polynomial Multiplication
# Course: CS7200
# Team:
# CHITROJU KODANDA SAIAYYAPPA RAGHAVENDRA SESHA NARAYANACHARYULU
# VARUN GRANDHI
# SUDHEER DANIEL MEGHAVARAM
############


degree = 0
count = 0
with open('input1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if count == 0:
            degree = int(line)
        elif count == 1:
            l1 = [int(i) for i in line.split(" ")]
        elif count == 2:
            l2 = [int(i) for i in line.split(" ")]
        count += 1

result = {}
for i in range(degree+2):
    result[i] = 0

step_count = 0
for i in range(len(l1)):
    for j in range(len(l2)):
        result[step_count+j] = result[step_count+j] + l1[i]*l2[j]
    step_count += 1

for i,j in result.items():
    print(j, end=" ")
