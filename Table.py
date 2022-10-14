table=int(input("Enter the number of table"))
i=table
for i in range(table,(table*10)+1,table):
    print("\n",i)
    

k=1
while k<11:
    print(f"{table} X {k} = {table*k}")
    k=k+1