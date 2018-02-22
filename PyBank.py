import os
import csv

#Reading in CSV file
Py1= os.path.join("budget_data_1.csv")

with open(Py1, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the first row of the csv
    next(csv_reader, None)

    Date= []
    revenue=[]
    inc_rev=[]
    maxim=0
    
    # Loop through rows
    for row in csv_reader:
          #print(row)
          Date.append(row[0]) #appending date into empty list
          revenue.append(int(row[1]))

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:" + " " + str(len(Date)))
    print("Total Revenue:" + " " + "$"+ str(sum(revenue)))
    

    for i in range(1, len(revenue)):
        change= revenue[i]-revenue[i-1]
        inc_rev.append(change)
        
    
      
    max_index= inc_rev.index(max(inc_rev))
    min_index= inc_rev.index(min(inc_rev))
    print("Average Revenue Change:" + " " +"$" + str(sum(inc_rev)/len(inc_rev)))
    print("Greatest Increase in Revenue:" +" " + Date[max_index+1] + " (" + str(inc_rev[max_index])+ ")")
    print("Greatest Decrease in Revenue:" +" " + Date[min_index+1] + " (" + str(inc_rev[min_index])+ ")")

    #print(inc_rev.index(max(inc_rev)))
    #print(inc_rev[max_index])
    #print(Date[max_index+1])
    
   # print("Greatest Increase in Revenue:"+" "+ str(max(inc_rev)))
