# https://www.hackerrank.com/challenges/finding-the-percentage
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
dc = dict()
lst1 = list()
# makes a dictonary with all names and test marks, defined by the value given earlier
for i in range(N):
    a = raw_input()
    # splits lst1 by spaces
    lst1 = a.split()
    # makes d the student names
    d = lst1[0]
    # removes name from lst1
    lst1.remove(lst1[0])
    # creates newlst1 with all of the test marks
    newlst1 = list(map(float, lst1))
    #adds the value of newlst1 to a new entry of dict dc
    dc[d] = newlst1
name = raw_input()
total = 0
if name in dc:
    # make marks equal to the given name of the student
    marks = dc[name]
    no = len(marks)
    for num in marks:
        total += num
avg = total / no
print "%.2f" % avg
