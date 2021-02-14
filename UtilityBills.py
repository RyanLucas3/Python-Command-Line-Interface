#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:03:42 2019

@author: ryanlucas
"""
from datetime import date, timedelta

def readConsumerInfo(file): 
#This function downloads the data from the file
#and converts it to a form that is usable in our program
    bills = []
    results = open(file, "r")
    for line in results:
        if line != "" and line != '\n':
            bill = line.strip().split(',')
            bill[0] = bill[0].title()
            bill[2] = int(bill[2])
            bill[3] = int(bill[3])
            bill[4] = int(bill[4])
            bill[5] = float(bill[5])
            bills.append(bill)
    results.close()
    return bills

def write_utility_bills(bills, file):
#This function writes the billing information to the file as string
    results = open(file, "w")
    for bill in bills:
        bill[2] = str(bill[2])
        bill[3] = str(bill[3])
        bill[4] = str(bill[4])
        bill[5] = str(bill[5])
        results.write(','.join(bill) + '\n')
    results.close()
   
def get_input(question, typeOfInput):
#We will attempt to get string input from the user. If it's invalid, we throw an error
#to tell the user that this input is not accepted.
    value = None
    while value == None:
        try:
            value = input(question).title().strip()
            if value != None and ',' not in value:
                return typeOfInput(value)
        except:
            print("Thats not a valid input. Please try again!")
            value = None

def get_amount():
#We will attempt to ask the user the billing amount
#If their answer is not convertible to a float we throw an error
    dueAmt = None
    while dueAmt == None:
        dueAmt = get_input("What is the amount on the bill?: ", float)
        if ',' not in str(dueAmt):
            return dueAmt
        else:
            print("Thats not a valid input. Please try again!")
            dueAmt = None

def get_Y():
#We will attempt to get the year as input from the user. If it's not in the range of possible years or
#Not convertible to an int, we throw an error.
    value = None
    while value == None :
        value = get_input("What year is the Bill from?: ", int)
        if value in range(1000,2050) and ',' not in str(value):
            return value
        else:
            print("Thats not a valid input. Please try again!")
            value = None

def get_debit_or_credit():
#We want to know if the bill is a debit or credit
#If the input is not equal to debit or credit. We will ask the user to try again
    d_or_c_Input = None
    while d_or_c_Input == None:
        d_or_c_Input = get_input("Is your bill a debit or a credit?: ", str).lower()
        if 'debit' == d_or_c_Input or 'credit' == d_or_c_Input:
            return d_or_c_Input
        else:
            print("That is not a valid input. Please use debit or credit. Please check your spelling")
            d_or_c_Input = None

def get_M():
#We will attempt to get the month as input from the user. If it's not in the range of possible months or
#Not convertible to an int, we throw an error.
    value = None
    while value == None:
        value = get_input("What month is the Bill from? Please use the MM format: ", int)
        if value in range(1,13) and ',' not in str(value):
            return value
        else:
            print("Thats not a valid input. Try again!")
            value = None

def get_Day(dueMonth, dueYear):
#We will attempt to get the day as input from the user given the month and year they have selected
#If it's not in the range of possible days or
#not convertible to an int, we throw an error.
    dueDay = None
    while dueDay == None:
        dueDay = get_input("What day is the bill due? Please use the DD format: ", int)
        if dueDay <= int(validDay(dueMonth, dueYear)) and ',' not in str(dueDay) and dueDay > 0:
            return dueDay
        else:
            print("Thats not a valid input. Try again!")
            dueDay = None
    
def validDay(month, year):
#This function determines how many days are in a month, given a month and a year as input
    try:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            days_in_months = {'1': '31', '2': '28', '3': '31', '4':'30', '5': '31', '6': '30','7' : '31', '8': '31','9': '30', '10': '31', '11':'30', '12': '31'}
        else:
            days_in_months = {'1': '31', '2': '29', '3': '31', '4':'30', '5': '31', '6': '30','7' : '31', '8': '31','9': '30', '10': '31', '11':'30', '12': '31'}
        return((days_in_months[str(month)]))
    except KeyError:
        print("That is not a valid combination of days, months and years")
  
def write_new_user_info(bill, file):
#This function takes a bill as input and appends it to the file.
#In effect, it will take the data from the questionnaire and 
#append it to the file
    try:
        results = open(file, "a")
        results.write(bill)
    except TypeError:
        print("Your details could not be written at this time")
    
def customerQuestionnaire():
#This function takes input from the user and creates a new bill array with their details
#This bill will then be added to the current database of files in another function
    companyName = get_input("What provider are you with?: ", str)
    customerName = get_input("What is your name?: ", str)
    dueYear = get_Y()
    dueMonth = get_M()
    dueDay = get_Day(dueMonth, dueYear)
    dueAmt = get_amount()
    debitRCredit = get_debit_or_credit()
    try:
        bill = [str(companyName), str(customerName), str(dueYear), str(dueMonth), str(dueDay), str(dueAmt), str(debitRCredit)]
        return (',').join(bill)
    except:
        print("Sorry your details could not be written at this time")

def total_debited_or_credited(year, bills, DOrC):
#User can input what year they want to find the total credit for
#E.g yearCreditAmtCount(2016) gives the total amount credited for all bills registered for 2016
    DebitOrCredit = 0
    for i in range(len(bills)):
        if int(bills[i][2]) == int(year):
            if DOrC in str(bills[i][6]):
                DebitOrCredit += float(bills[i][5])
    return round(DebitOrCredit,2)

def highestAmount(debitORcredit, bills):
#User can input whether they want to find the bill with the highest outstanding credit or highest outstanding debit
#E.g highestAmount('debit') gives the highest debit balance on any account
    DebitsORCredits = []
    for i in range(len(bills)):
        if debitORcredit in bills[i][-1]:
            DebitsORCredits.append(float(bills[i][5]))
    try:
        return('The maximum ' + debitORcredit  + ' on any account is ' + str(max(DebitsORCredits)))
    except:
        return("There are no " + debitORcredit + " bills")

def uniqueBills(bills):
#We want to display the totals for each year. For example, there may be multiple entries for a particular year,
#But we want to use a particular year just once since we want the total.
#Thus we want a list of bills for unique years
    newBills = []
    for i in range(len(bills)):
        if bills[i][2] not in newBills:
            newBills.append(bills[i][2])
    return newBills

def format_unique_bills(sortedByDate):
#This function formats the uniqueBills function to display it to the user in
#a digestible way
    newBills = uniqueBills(sortedByDate)
    for j in newBills:
        print(j," " * 18,'€',total_debited_or_credited(j, bills, 'debit')," " * 20,'€',total_debited_or_credited(j, bills, 'credit'))
    return ""

def billCount(company, bills):
    #We want to count how many bills belong to a particular company  
    companiesCount = {}
    newBills = []
    for i in range(len(bills)):
        if bills[i][0] not in newBills:
            dicti = {bills[i][0]: 1}
            companiesCount.update(dicti)
            newBills.append(bills[i][0])
        elif bills[i][0] in newBills:
            companiesCount[bills[i][0]] += 1
    try:
        if company != '':
            if int(companiesCount[str(company)]) > 1:
                return(company +  " have " + str(companiesCount[str(company)]) + " bills on their file")
            elif int(companiesCount[str(company)]) == 1:
                return(company +  " have " + str(companiesCount[str(company)]) + " bill on their file")
        else:
            return("You can't have a blank company")
    except:
        return("We dont have that company on our file!")

def averageSpendPY(year,bills):
#Provides a report to calculate the average spent in a particular year.
#Year is specified by the user.   
    yearly_spend = 0
    numberOfElements = 0
    for i in range(len(bills)):
        if int(year) == int(bills[i][2]):
            yearly_spend += float(bills[i][5])
            numberOfElements += 1
    try:
        average_spend = yearly_spend/numberOfElements
        return(average_spend)
    except ZeroDivisionError:
        return 0
        print("There are no bills in this year. Hence, there is no average!")

def averageSpendPM(month, year,bills):
#Provides a report to calculate the average spent in a particular month in a particular year.
#Month and year are specified by the user.
    monthly_spend = 0
    numberOfElements = 0
    for i in range(len(bills)):
        if int(year) == int(bills[i][2]):
            if int(month) == int(bills[i][3]):
                monthly_spend += float(bills[i][5])
                numberOfElements += 1
    try:
        averageM_spend = monthly_spend/numberOfElements
        return averageM_spend
    except ZeroDivisionError:
        return 0
        
def specificMonth(yearChoice):
#The user will be asked if they want to view bills for a specific month
#If they say no, they will get the average spend for the year of their choosing
    YesNah = None
    while YesNah == None:
        YesNah = get_input('Are you looking for a specific month? Please use yes or no: ', str)
        try:
            if YesNah != None:
                if 'n' in YesNah.lower() or 'no' in YesNah.lower():
                    return("The average spend for " + yearChoice + " is " + str(averageSpendPY(int(yearChoice)), bills))
                elif 'yes' in YesNah.lower() or 'y' in YesNah.lower():
                    return get_M()
                else:
                    print('Thats not a valid input. Please use yes or no')
                    specificMonth(yearChoice)
        except:
            return("Thats not a valid input, Please try again!")
            YesNah = None
        
def averageSpendInPeriod(bills):
#If the user has a month choice i.e. they're looking for a specific month, we return the avg for the month
#Otherwise, we simply return the average for the year.
    yearChoice = get_Y()
    monthChoice = specificMonth(yearChoice)
    try:
        if monthChoice != None:
            if int(monthChoice) in range(1,13) and averageSpendPM(int(monthChoice), int(yearChoice), bills) != None:
                return("The average spend for " + str(monthCreator(int(monthChoice))) + " in " + str(yearChoice) + " is " + str(averageSpendPM(int(monthChoice), int(yearChoice),bills)))
            else:
                return("Since there are no bills, hence there is no average")
    except:
        return("The average spend for " + str(yearChoice) + " is " + str(averageSpendPY(int(yearChoice), bills)))
        
def mostPopularCompany(bills):
#Counts the number of bills attributable to each company.
#Then finds the maximum of those.
    companiesCount = {}
    newBills = []
    for i in range(len(bills)):
        try:
            if bills[i][0] not in newBills:
                dicti = {bills[i][0]: 1}
                companiesCount.update(dicti)
                newBills.append(bills[i][0])
            elif bills[i][0] in newBills:
                companiesCount[bills[i][0]] += 1
        except:
            companiesCount = None
    return max_of_a_dictionary(companiesCount)
    
def max_of_a_dictionary(companiesCount):
#This function checks to see whether there is 1 maximum or 2 maximum values,
#given a list of companies    
    maximumValues = 1
    try:
        if companiesCount != None:
            maximum = max(companiesCount, key = companiesCount.get)
            for s,v in companiesCount.items():
                if companiesCount[s] == companiesCount[maximum] and s != maximum:
                    return('There are two companies that are equally the most popular' + '\n' + 'One of them is ' + max(companiesCount, key = companiesCount.get) + " and the other is " + s + ".")
                    maximumValues = 2
            if maximumValues != 2:
                return("The company with the most bills on any account is " +  max(companiesCount, key = companiesCount.get).title())
            else:
                return("There are no companies listed")
    except:
        return("There are no companies listed")
           
def datesSorted(bills):
#Sorts the matrix but starts in the 3rd column rather than the first,
#Since we are sorting by date rather than alphabetically
#We use the reverse parameter because by default it would sort starting with the smallest number.
    sort1 = sorted(bills, key= lambda bills: (bills[2], bills[3], bills[4]), reverse = True)
    return sort1

def timeBetweenDates(sortedList):
#This function uses the datetime framework and finds the time elapsed between all bills
#And divides it by the total number of bills
    orderedFormattedDates = []
    delta = []
    try:
        for i in range(len(sortedList)):
            orderedFormattedDates.append(date(int(sortedList[i][2]), int(sortedList[i][3]), int(sortedList[i][4])))
        for i in range(len(orderedFormattedDates)-1):
            delta.append(orderedFormattedDates[i] - orderedFormattedDates[i+1])
        averageTime = sum(delta,timedelta()) / len(delta)
        return("The average amount of time between bills is " + str(averageTime))
    except ZeroDivisionError:
        return("There are no bills and hence there is no average time between them")

def monthCreator(month):
#This function takes a number as input e.g 4 and converts it to a month in word form
#For example, 4 will convert to April, since April is the fourth month!
    months = {'1': 'January' , '2': 'February','3': 'March','4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    try:
        return months[str(month)]
    except:
        return("That is not a real month!")

def display_all_bills(bills):
#This function formats the bill display bills option (Main Menu option 3)
#so that it is in a nice, presentable table
    print('============================================ ============================================== =============================================== ====================== =========================')
    print('                Company Name                                  Customer Name                                        Date                              Amount             Debit or Credit')
    print('============================================ ============================================== =============================================== ====================== =========================')
    for i in range(len(bills)):
        print('             {:^20}                        {:^20}                                {:^5}/{:^5}/{:^5}                  {:^15}            {:^5}'.format(bills[i][0], bills[i][1], bills[i][2], bills[i][3], bills[i][4], bills[i][5], bills[i][6]))
        print('============================================ ============================================== =============================================== ====================== =========================')

def format_report(func):
#This function formats any reports by putting a header line and a final line between the report information
    print('----------------------------------------------------------------')
    print(func)
    print('----------------------------------------------------------------')
    return('')
    
def format_title(title):
#This function puts a title at the centre. It is mainly for visual effect.
    print(' ------------------------------------------ ')
    print('|','{:^40}'.format(str(title)),'|')
    print(' ------------------------------------------ ')

def process_report_choice_1():
    format_title('Total Billing Report')
    print("Year", " "* 13, "Total Debited", " " * 16, "Total Credited")
    format_report(format_unique_bills(datesSorted(bills)))
    process_report_choice(bills)

def process_report_choice_2():
    format_title('Most Popular Company')
    print(format_report(mostPopularCompany(bills)))
    process_report_choice(bills)
    
def process_report_choice_3():
    format_title('Bills by Date')
    display_all_bills(datesSorted(bills))
    process_report_choice(bills)
    
def process_report_choice_4():
    format_title('Highest Debit')
    print(format_report(highestAmount('debit', bills)))
    process_report_choice(bills)
    
def process_report_choice_5():
    format_title('Highest Credit')
    print(format_report(highestAmount('credit', bills)))
    process_report_choice(bills)

def process_report_choice_6():
    format_title('Total Bills by Company')
    print(format_report(billCount(get_input("What company are you lookin for?: ", str).title(), bills)))
    process_report_choice(bills)

def process_report_choice_7():
    format_title('Average Spend by Period')
    print(format_report(averageSpendInPeriod(bills)))
    process_report_choice(bills)

def process_report_choice_8():
    format_title('Average Time Between Bills')
    print(format_report(timeBetweenDates(datesSorted(bills))))
    process_report_choice(bills)
   
def process_report_choice(bills):
#This function takes info from the user about what report they want to view.
#It will then call the respective report that the user wishes to view. 
    format_title(('reports'))
    print("1. Total Billing Report\n\n2. Most Popular Company\n\n3. Bills by Date\n\n4. Highest Debit\n\n5. Highest Credit\n\n6. Total Bills by Company\n\n7. Average Spend by Period\n\n8. Average Time Between Bills\n\n9 Go back to main menu.")
    print('---------------------------------------')
    reportChoice = get_input("What report would you like to access?: ", str)
    while reportChoice != '15':
        if reportChoice == "1":
            process_report_choice_1()
        elif reportChoice == "2":
            process_report_choice_2()
        elif reportChoice == "3":
            process_report_choice_3()
        elif reportChoice == "4":
            process_report_choice_4()
        elif reportChoice == "5":
            process_report_choice_5()
        elif reportChoice == "6":
            process_report_choice_6()
        elif reportChoice == "7":
            process_report_choice_7()
        elif reportChoice == "8":
            process_report_choice_8()
        elif reportChoice == '9':
            mainFunction(bills)
        else:
            format_report('Invalid Option')

def process_main_choice_no_1():
    format_title('Enter your details')
    write_new_user_info(customerQuestionnaire(), file)
    format_report(("Congrats! Your details were written to the file!"))
    mainFunction(bills)

def process_main_choice_no_2():
    process_report_choice(bills)
    mainFunction(bills)

def process_main_choice_no_3():
    format_title('All Bills')
    print(display_all_bills(bills))
    mainFunction(bills)
  
def process_main_choice_no_4():
    format_title('Terms and Conditions')
    print("""We are the best Utility Bills company and we treat our customers like royalty""")
    mainFunction(bills)
    
def process_main_choice_no_5():
    format_title('About the author')
    print('    ____                       __                         ')
    print('   / __ \__  ______ _____     / /   __  ___________ ______')
    print('  / /_/ / / / / __ `/ __ \   / /   / / / / ___/ __ `/ ___/')
    print(' / _, _/ /_/ / /_/ / / / /  / /___/ /_/ / /__/ /_/ (__  )')
    print('/_/ |_|\__, /\__,_/_/ /_/  /_____/\__,_/\___/\__,_/____/') 
    print('      /____/                                            ')
    print('Ryan has some prior programming experience. He has played around with Swift before and built some very basic applications, but he is completely new to Python!')
    print('--------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------')
    mainFunction(bills)

def process_main_choice_no_6():
    format_title('Thank you for using the program!')
    print("GoodBye")
    quit()
    
def process_main_choice(choice, bills):
#This function takes info from the user about what Main Menu option they want.
#It will then call the option that the user has chosen and bring them to
#that respective section/sub-menu.
    while choice != '9':
            if choice == "1":
                process_main_choice_no_1()
            elif choice == '2':
                process_main_choice_no_2()
            elif choice == "3":
                process_main_choice_no_3()
            elif choice == "4":
                process_main_choice_no_4()
            elif choice == '5':
                process_main_choice_no_5()
                choice = '9'
            elif choice == "6":
                process_main_choice_no_6()
                choice = '9'
            else:
                format_report('Invalid option')
                mainFunction(bills)  
    
def mainFunction(bills):
#This function is called at the beginning of the program and it displays the main menu.
#Aswell as giving the user the option to select from that main menu. 
    format_title('Main Menu')
    print("1. Add Bill\n\n2. Generate Reports\n\n3. Display All Bills\n\n4. Read T&C\n\n5. About the Author\n\n6. Quit")
    print('----------------------------------------------')
    choice = get_input("Please choose option: ", str)
    process_main_choice(choice, bills) 

def press_any_key_to_enter(bills):
#This begins the program. The user simply presses any key to begin using the program
    user_key = None
    user_key = input("Press any key to enter: ")
    if user_key != None:
        mainFunction(bills)

def get_file(file):
    try:
        new = open(file)
        new.close()
        return file
    except:
        print("File not found. Please try again")
        return None

def entry_screen_UI():
    print('__          __  _                            _          _   _                  _   _ _ _ _           _     _ _ _                                                 _)  ')
    print('\ \        / / | |                          | |        | | | |                | | (_) (_) |         | |   (_) | |                                                 | |')
    print(' \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___   _   _| |_ _| |_| |_ _   _  | |__  _| | |___    ___ ___  _ __ ___  _ __   __ _ _ __  _   _| |')
    print('  \ \/  \/ / _ \ |/ __/ _ \|  _   _ \ / _ \ | __/ _ \  | __|  _ \ / _ \ | | | | __| | | | __| | | | | |_ \| | | / __|  / __/ _ \|  _   _ \|  _ \ / _  |  _ \| | | | |')
    print('   \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | |_| | |_| | | | |_| |_| | | |_) | | | \__ \ | (_| (_) | | | | | | |_) | (_| | | | | |_| |_|')
    print('    \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|  \__,_|\__|_|_|_|\__|\__, | |_.__/|_|_|_|___/  \___\___/|_| |_| |_| .__/ \__,_|_| |_|\__, (_)')
    print('                                                                                             __/ |                                        | |                 __/ |   ')
    print('                                                                                             |___/                                        |_|                |___/   ')
    EntryScreen =     """                
                                                        ____________________________________________________
                                                       /                                                     \ 
                                                       |   |                                             |    |
                                                       |   |  C:\> _ Hey Darren! Welcome to the utility  |    |
                                                       |   |  bills company. Press any key to enter      |    |
                                                       |   |  the program                                |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |                                             |    |
                                                       |   |_____________________________________________|    |
                                                       |                                                      |
                                                        \_____________________________________________________/
                                                               \_______________________________________/
                                                            _______________________________________________
                                                         _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
                                                      _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
                                                   _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
                                                _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
                                             _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
                                            :-----------------------------------------------------------------------------:
                                            `---._.-----------------------------------------------------------------._.---'
                            
                            
                                """
    print(EntryScreen)
    print("Please use full screen on terminal for improved UI ;)")
        
if __name__ == '__main__':
    file = None
    from sys import argv
    if len(argv) == 2:
        file = get_file(argv[1])
    while file == None:
        file = get_file(get_input("What is your file name: ", str))
    bills = readConsumerInfo(file)     
    entry_screen_UI()
    press_any_key_to_enter(bills)
    write_utility_bills(bills, file) 
