x,y=[int(i) for i in input().strip().split()]
main_matrix=[]
for i in range(0,x):
    ele=[i for i in input().split()]
    main_matrix.append(ele)
z=int(input())

for i in range(0,x-z+1):
    for j in range(0,y-z+1):
        if len(list(set([main_matrix[i][j],main_matrix[i+z-1][j],main_matrix[i][j+z-1],main_matrix[i+z-1][j+z-1]])))==1:
            for a in range(0,z):
                main_matrix[i+a][j+a]='*'
                main_matrix[i+a][z+j-a-1]="*"
for i in range(0,x):
    for j in range(0,y):
        print(main_matrix[i][j],end=" ")
    print()    
