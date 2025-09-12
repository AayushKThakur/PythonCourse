#Print 1 to 10
for i in range(1, 11): #left value is included and right excluded
    print(i, end=" ")
print(" ")
#print 1 to 20...1 3 5 7 9...19
for i in range(1,21,2):
    print(i,end=" ")
print(" ")

#print 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")
print(" ")
#print sum of all numbers divisibile by 4 from 20 to 50
total=0
for i in range(20, 51):
    if i%4==0:
        total=total+i
print(total)