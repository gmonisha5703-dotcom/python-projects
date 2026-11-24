# Sales Data Analysis Project

import statistics

print("===== SALES DATA ANALYSIS =====")

sales = [1200, 1500, 1800, 2000, 2500, 2200, 3000]

total_sales = sum(sales)
average_sales = statistics.mean(sales)
highest_sales = max(sales)
lowest_sales = min(sales)

print("Daily Sales:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)

print("\n===== SALES REPORT =====")

if average_sales >= 2000:
    print("Sales Performance: Excellent")
elif average_sales >= 1500:
    print("Sales Performance: Good")
else:
    print("Sales Performance: Needs Improvement")

print("Analysis Completed Successfully!")
