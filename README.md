# Utility_bills
Program for a utility provider to track customer information.

Dublin Bill Management Company is a start-up bill management company, i.e., they offer tracking for electricing, gas, and utility bills.

I have developed a command line interface python system that will record all of their customers bills, together with a menu to generate queries/reports that can be run against this data.

The following is some sample customer data that you should make use of (the full list is available as the file results.csv given):
  Electric Ireland, John Smyth, 2017, 05, 12, 11.58, credit
  Energia, Missy May, 2016, 12, 22, 122.52, debit
  Vodafone, John Smyth, 2016, 11, 17, 20.00, debit
  Energia, Susie Sue, 2016, 11, 03, 25.00, debit
  Vodafone, Susie Sue, 2016, 11, 17, 5.00, credit

Data Description

The file is a comma separated value (csv) file – each field is separated by a comma. The first field is the utility company, the second is the customer name, the third is the year, fourth is the month, fifth is the day, i.e. date  (in YYYY, MM, DD format), the sixth field is the amount of the bill, while the last field is a flag indicating whether this is a credit or debit against the bill.
 
Reports/Queries
1.	I will provide a way for a user to enter utility bill details: utility company, name of the customer, date of the bill, the amount, and a flag indicating whether the bill is debit or credit.
2.	I will start my code with the initial results.csv above
3.	I will provide a report that lists years, total credited and total debited, e.g., the output will look like the following:
Year		Total Credited	Total Debited
2016		   €123.45		     €678.90
2017		   €543.21		     €987.60

4.	I will provide a report that shows the most popular utility company.  The most popular utility company is the one with the most bills against that provider.

5.	I will provide a report that shows the bills in date order.
6.	I will provide another report that displays the highest amount for a bill that is a credit, and one for a debit.
7.	I will provide a report to indicate how successful the company is.  This will display the total number of bills.
8.	I will provide a report to calculate the average spent per period of time (month/year) that can be entered by the user.
9.	I will provide a report to calculate the average time between bills.

