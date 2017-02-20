N = int(raw_input())
grades = {}
for i in range(N):
    in_line = raw_input()
    line = in_line.split(' ')
    grades[line[0]] = [float(x) for x in line[1:]]

lookup = raw_input()
print sum(grades[lookup])/(3.0)
