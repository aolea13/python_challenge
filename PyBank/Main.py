#Import Dependencies
import os
import csv

#Print Header
print("")
print("Financial Analysis")
print("________________________")
print("")

#Declare file location path
file_path = os.path.join("/Users/austinolea/Desktop/GIT_REPOS/python_challenge/Resources/budget_data.csv")

#Create lists to store pulled data/iterate through
total_months = []
total_profit_loss = []
monthly_profit_loss_change = []

#Open CSV
csv_file = open(file_path)
csv_reader = csv.reader(csv_file)
next(csv_reader)

 #Iterate through CSV data to populate lists
for each_row in csv_reader:
        #Append lists
        total_months.append(each_row[0])
        total_profit_loss.append(int(each_row[1]))

#Iterate through the total_profit_loss list
for x in range(len(total_profit_loss ) - 1):
        #Take the difference between two months and append to coresponding list
        monthly_profit_loss_change.append(total_profit_loss [x + 1] - total_profit_loss [x])

#Obtain the max and min
max_increase = max(monthly_profit_loss_change)
max_decrease = min(monthly_profit_loss_change)

# Correlate max and min to the proper month
max_increase_month = monthly_profit_loss_change.index(max(monthly_profit_loss_change)) + 1 # The +1 Tells us to move a month
max_decrease_month = monthly_profit_loss_change.index(min(monthly_profit_loss_change)) + 1

# Print Statements
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: {round(sum(monthly_profit_loss_change ) / len(monthly_profit_loss_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

# Output files
output_file = os.path.join("/Users/austinolea/Desktop/GIT_REPOS/python_challenge/PyBank/analysis/summary.txt")


with open(output_file, "w") as file:
    # Write statments to print to summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit_loss)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_loss_change) / len(monthly_profit_loss_change), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")
