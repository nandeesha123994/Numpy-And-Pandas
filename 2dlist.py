#creating the 2d list

k=11
l=[]
a=[]
for i in range(3):
    for j in range(3):
        a.append(k)
        k=k+1
    l.append(a)
    a=[]
print(l)



#converting the list into matrxi

for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=" ")

    print()


# printing only diagonal values

for i in range(len(l)):
    for j in range(len(l[0])):
        if i==j:
         print(l[i][j],end=" ")

    print()

#printing the cross diagonal

for i in range(len(l)):
    for j in range(len(l[0])):
        if i+j==2:
         print(l[i][j],end=" ")

    print()

