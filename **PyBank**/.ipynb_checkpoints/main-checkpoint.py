import os
import csv

filepath = os.path.join('budget_data.csv')
output_path = os.path.join('financial_analysis.txt')

total_months = 0
total_net = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]

with open (filepath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    
    for row in csvreader:
        total_months = total_months + 1
        total_net += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

average_change = sum(net_change_list) / len(net_change_list)

output = (f'Financial Analysis\n'
          f'-------------------\n'
          f'Total Months: {total_months}\n'
          f'Total: ${total_net}\n'
          f'Average Change: ${average_change:.2f}\n'
          f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
          f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

print(output)

with open(output_path, "w") as txt_file:
    txt_file.write(output)
