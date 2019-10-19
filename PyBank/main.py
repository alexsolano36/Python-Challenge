#import modules
import os
import csv

#set correct path for csv file
PyBankcsv = os.path.join("Resources", "budget_data.csv")

#lists to store data
profit = []
monthly_changes = []
date = []

#make variables reset
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#open csv
with open(PyBankcsv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        
        #getting values for variables
        for row in csvreader:
            #number of months
            count = count +1
            date.append(row[0])
            
            #appending profit info for total profit
            profit.append(row[1])
            total_profit = total_profit + int(row[1])
            
            #calculate average monthly change
            final_profit = int(row[1])
            monthly_change_profits = final_profit - initial_profit
            
            #store changes
            monthly_changes.append(monthly_change_profits)
            total_change_profits = total_change_profits + monthly_change_profits
            initial_profit = final_profit
            
            #average change in profits
            average_change_profits = (total_change_profits/count)
            
            #max and min change in profits with dates
            greatest_increase_profits = max(monthly_changes)
            greatest_decrease_profits = min(monthly_changes)
            increase_date = date[monthly_changes.index(greatest_increase_profits)]
            decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
        
        print("Financial Analysis")
        print("Total Months: " + str(count))
        print("Total Profits: " + "$" + str(total_profit))
        print("Average Change: " + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits)+ ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        
with open('financial_analysis.txt', 'w') as text:
    text.write("   Financial Analysis" + "\n")
    text.write("      Total Months: " + str(count) + "\n")
    text.write("      Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("      Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("      Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits)+ ")\n")
    text.write("      Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")\n")
