numDays=int(input("Enter the number of days: "))
total=0
temp=[]

for i in range(numDays):
    nextDay=float(input("Enter the temperature for day "+str(i+1)+": "))
    temp.append(nextDay)
    total+=temp[i]
    
avg= round(total/numDays,2)
print("The average temperature is: ",str(avg))

above=0
for i in temp:
    if i>avg:
        above+=1
        
print("The number of days above average is: ",str(above))