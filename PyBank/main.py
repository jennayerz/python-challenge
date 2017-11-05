import csv

budget_data_1 = '/Users/Jenny/Desktop/NEW/python-challenge/PyBank/budget_data_1.csv'

# ---------------------------
# TOTAL MONTHS
# ---------------------------

with open(budget_data_1, newline='') as budget_data1:
    all_budget_data1 = csv.reader(budget_data1, delimiter=',')

#    print(all_budget_data1)

#    for row1 in all_budget_data1:
#        print(row1)

print("Financial Analysis")
print("-------------------------")

total_months = sum(1 for line in open(budget_data_1)) - 1
print("Total Months: " + str(total_months))

# ---------------------------
# TOTAL REVENUE
# ---------------------------

with open(budget_data_1, newline='') as budget_data1:
    all_budget_data1 = csv.reader(budget_data1, delimiter=',')

    next(all_budget_data1, None)
    total_rev1 = sum(int(r1[1]) for r1 in all_budget_data1)

total_revenue = str(total_rev1)
print("Total Revenue: $" + total_revenue)

# ---------------------------
# AVERAGE REVENUE CHANGE
# ---------------------------
with open(budget_data_1, newline='') as budget_data1:
    all_budget_data1 = csv.reader(budget_data1, delimiter=',')

    next(all_budget_data1, None)
    avg_rev1 = round(sum(int(r1[1]) for r1 in all_budget_data1) / sum(1 for line in open(budget_data_1)))

avg_rev = str(avg_rev1)
print("Average Revenue Change: $" + avg_rev)

# ---------------------------
# GREATEST INCREASE IN REVENUE
# ---------------------------
with open(budget_data_1, newline='') as budget_data1:
    all_budget_data1 = csv.reader(budget_data1, delimiter=',')

    next(all_budget_data1, None)    
    for row1 in all_budget_data1:
        max_rev1 = max(row1[1] for row1 in all_budget_data1)
        row1_edit = str(row1).replace("'", "")
        row1_edit1 = str(row1_edit).replace(" ", "$")
        row1_edit2 = str(row1_edit1).replace("[", "")
        row1_edit3 = str(row1_edit2).replace(",", " (")
        row1_edit4 = str(row1_edit3).replace("]", ")")
        print("Greatest Increase in Revenue: " + row1_edit4)

# ---------------------------
# GREATEST DECREASE IN REVENUE
# ---------------------------
with open(budget_data_1, newline='') as budget_data1:
    all_budget_data1 = csv.reader(budget_data1, delimiter=',')

    next(all_budget_data1, None)    
    for r1 in all_budget_data1:
        min_rev1 = min(r1[1] for r1 in all_budget_data1)
        print("Greatest Decrease in Revenue: " + str(r1[0]) + " ($" + min_rev1 + ")")




# -----------------------------------------------
# FOR BUDGET_DATA_2.CSV
# import csv

# budget_data_2 = '/Users/Jenny/Desktop/NEW/python-challenge/PyBank/budget_data_2.csv'

# ---------------------------
# TOTAL MONTHS
# ---------------------------
#with open(budget_data_2, newline='') as budget_data2:
#    all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data2, None)

#    for row2 in all_budget_data2:
#        print(row2)

#total_months2 = + sum(1 for line in open(budget_data_2)) - 1
#print("Total Months: " + str(total_months))

# ---------------------------
# TOTAL REVENUE
# ---------------------------

#with open(budget_data_2, newline='') as budget_data2:
#    all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data2, None)
#    total_rev2 = sum(int(r2[1]) for r2 in all_budget_data2)

#total_revenue = str(total_rev2)
#print("Total Revenue: $" + total_revenue)

# ---------------------------
# AVERAGE REVENUE
# ---------------------------
#with open(budget_data_2, newline='') as budget_data2:
#    all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data2, None)
#    avg_rev2 = round(sum(int(r2[1]) for r2 in all_budget_data2) / sum(1 for line in open(budget_data_2)))

#avg_rev = str(avg_rev2)
#print("Average Revenue Change: $" + avg_rev)

# ---------------------------
# GREATEST INCREASE IN REVENUE
# ---------------------------
#with open(budget_data_2, newline='') as budget_data2: 
#    all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data1, None)
#    for row2 in all_budget_data2:
#        max_rev2 = max(row2[1] for row2 in all_budget_data2)
#        print(row2)

# ---------------------------
# GREATEST INCREASE IN REVENUE
# ---------------------------
#with open(budget_data_2, newline='') as budget_data2:
    #all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data2, None)    
#    for row2 in all_budget_data2:
#        max_rev2 = max(row2[1] for row2 in all_budget_data1)
#        row2_edit = str(row2).replace("'", "")
#        row2_edit1 = str(row2_edit).replace(" ", "$")
#        row2_edit2 = str(row2_edit1).replace("[", "")
#        row2_edit3 = str(row2_edit2).replace(",", " (")
#        row2_edit4 = str(row2_edit3).replace("]", ")")
#        print("Greatest Increase in Revenue: " + row2_edit4)

# ---------------------------
# GREATEST DECREASE IN REVENUE
# ---------------------------
#with open(budget_data_2, newline='') as budget_data2:
#    all_budget_data2 = csv.reader(budget_data2, delimiter=',')

#    next(all_budget_data2, None)    
#    for r2 in all_budget_data2:
#        min_rev2 = min(r2[1] for r2 in all_budget_data2)
#        print("Greatest Decrease in Revenue: " + str(r2[0]) + " ($" + min_rev2 + ")")
