#Importing Decimal and csv functions
from decimal import Decimal
import csv

#Initial empty list
sales_regions = []

##Initial values of the variables of interest

#Number of units sold for each region
units_sold_Australia_Oceania = 0
units_sold_Central_America_Caribbean = 0
units_sold_Europe = 0
units_sold_Sub_Saharan_Africa = 0
units_sold_Asia = 0
units_sold_Middle_East_North_Africa = 0
units_sold_North_America = 0

#Number of countries within each region
Australia_Oceania_number = 0
Central_America_Caribbean_number = 0
Europe_number = 0
Sub_Saharan_Africa_number = 0
Asia_number = 0
Middle_East_North_Africa_number = 0
North_America_number = 0

#Revenue of all units sold for each region
units_revenue_Australia_Oceania = 0
units_revenue_Central_America_Caribbean = 0
units_revenue_Europe = 0
units_revenue_Sub_Saharan_Africa = 0
units_revenue_Asia = 0
units_revenue_Middle_East_North_Africa = 0
units_revenue_North_America = 0

#Total revenue, average revenue and number of units for all regions
total_units_sold = 0
total_units_number = 0
total_revenue = 0

#Reading the file as a csv while skipping the first row (titles)
with open ('input_files/100_sales_recs.csv', encoding = 'utf-8') as file_object:
    next(file_object)
    csv_file_object = csv.reader(file_object)

    for row in csv_file_object:
        sales_regions.append(row[0])
        total_units_sold += Decimal(row[8])
        total_units_number += 1
        total_revenue += Decimal(row[11])

        if row[0] == 'Asia':
            Asia_number += 1
            units_sold_Asia += Decimal(row[8])
            units_revenue_Asia += Decimal(row[11])

        elif row[0] == 'Australia and Oceania':
            Australia_Oceania_number += 1
            units_sold_Australia_Oceania += Decimal(row[8])
            units_revenue_Australia_Oceania += Decimal(row[11])

        elif row[0] == 'Central America and the Caribbean':
            Central_America_Caribbean_number += 1
            units_sold_Central_America_Caribbean += Decimal(row[8])
            units_revenue_Central_America_Caribbean += Decimal(row[11])

        elif row[0] == 'Europe':
            Europe_number += 1
            units_sold_Europe += Decimal(row[8])
            units_revenue_Europe += Decimal(row[11])

        elif row[0] == 'Middle East and North Africa':
            Middle_East_North_Africa_number += 1
            units_sold_Middle_East_North_Africa += Decimal(row[8])
            units_revenue_Middle_East_North_Africa += Decimal(row[11])

        elif row[0] == 'North America':
            North_America_number += 1
            units_sold_North_America += Decimal(row[8])
            units_revenue_North_America += Decimal(row[11])

        elif row[0] == 'Sub-Saharan Africa':
            Sub_Saharan_Africa_number += 1
            units_sold_Sub_Saharan_Africa += Decimal(row[8])
            units_revenue_Sub_Saharan_Africa += Decimal(row[11])

##Printing the values of interest

#Header
print(" "*40, end="")
print('Sales Report')
print(" "*40, end="")
print("------------")
print()
print(" "*35, end="")
print('Produced on: 2022-07-28')
print()
print("Total, 7 regions.")
print()

#Sorting the list of regions into a set of regions
sales_regions_sorted = sorted(set(sales_regions))

#List of regions analysed
print(f'Regions analysed: {sales_regions_sorted[0]}, {sales_regions_sorted[1]}, {sales_regions_sorted[2]}, {sales_regions_sorted[3]}, {sales_regions_sorted[4]}, {sales_regions_sorted[5]} and {sales_regions_sorted[6]}.')
print()

#Total sales for Asia
print(sales_regions_sorted[0])
print()
print('{0:30s}{1:0.2f}'.format('Total units sold: ', units_sold_Asia))
print('{0:30s}${1:0.2f}'.format('Average revenue per unit: ', (units_revenue_Asia / Asia_number)))
print('{0:30s}${1:0.2f}'.format('Total revenue of sales: ', units_revenue_Asia))
print()

#Total sales for Australia Oceania
print(sales_regions_sorted[1])
print()
print('{0:30s}{1:0.2f}'.format('Total units sold: ', units_sold_Australia_Oceania))
print('{0:30s}${1:0.2f}'.format('Average revenue per unit: ', (units_revenue_Australia_Oceania / Australia_Oceania_number)))
print('{0:30s}${1:0.2f}'.format('Total revenue of sales: ', units_revenue_Australia_Oceania))
print()

#Total sales for Central America, Caribbean
print(sales_regions_sorted[2])
print()
print('{0:30s}{1:0.2f}'.format('Total units sold: ', units_sold_Central_America_Caribbean))
print('{0:30s}${1:0.2f}'.format('Average revenue per unit: ', (units_revenue_Central_America_Caribbean / Central_America_Caribbean_number)))
print('{0:30s}${1:0.2f}'.format('Total revenue of sales: ', units_revenue_Central_America_Caribbean))
print()

#Total sales for Europe
print(sales_regions_sorted[3])
print()
print('{0:30s}{1:.2f}'.format('Total units sold: ', units_sold_Europe))
print('{0:30s}${1:.2f}'.format('Average revenue per unit: ', (units_revenue_Europe / Europe_number)))
print('{0:30s}${1:.2f}'.format('Total revenue of sales: ', units_revenue_Europe))
print()

#Total sales for Middle East North Africa
print(sales_regions_sorted[4])
print()
print('{0:30s}{1:.2f}'.format('Total units sold: ', units_sold_Middle_East_North_Africa))
print('{0:30s}${1:.2f}'.format('Average revenue per unit: ', (units_revenue_Middle_East_North_Africa / Middle_East_North_Africa_number)))
print('{0:30s}${1:.2f}'.format('Total revenue of sales: ', units_revenue_Middle_East_North_Africa))
print()

#Total sales for North America
print(sales_regions_sorted[5])
print()
print('{0:30s}{1:.2f}'.format('Total units sold: ', units_sold_North_America))
print('{0:30s}${1:.2f}'.format('Average revenue per unit: ', (units_revenue_North_America / North_America_number)))
print('{0:30s}${1:.2f}'.format('Total revenue of sales: ', units_revenue_North_America))
print()

#Total sales for Sub-Saharan Africa
print(sales_regions_sorted[6])
print()
print('{0:30s}{1:.2f}'.format('Total units sold: ', units_sold_Sub_Saharan_Africa))
print('{0:30s}${1:.2f}'.format('Average revenue per unit: ', units_revenue_Sub_Saharan_Africa / Sub_Saharan_Africa_number))
print('{0:30s}${1:.2f}'.format('Total revenue of sales: ', units_revenue_Sub_Saharan_Africa))
print()

#Big totals
print('Grand Totals')
print()
# print('Total units sold: {}'.format(total_units_sold))
print('{0:30s}{1:.2f}'.format("Total units sold: ", total_units_sold))
print('{0:30s}${1:.2f}'.format("Average revenue per unit: ", total_revenue / total_units_number))
print('{0:30s}${1:.2f}'.format("Total revenue of sales: ", total_revenue))




