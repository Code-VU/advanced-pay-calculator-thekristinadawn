def calculatePay():
    
    # This first line is provided for you
try:
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    hours = float(hrs)
    pay = float(rate)
    if hours <=40:
        TotalPay=(hrs*pay)
    elif hours > 40:
        TotalPay=(40*pay) + (hours-40)*1.5*pay

    print("Enter Hours:",hrs)
    print("Enter Rate:",rate)
    print ("Pay:",TotalPay)
    
except: 
        print('Please enter a numeric value.')

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()