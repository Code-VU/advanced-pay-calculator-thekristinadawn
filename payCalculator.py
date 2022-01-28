def calculatePay():
    
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    if hrs <=40:
        TotalPay=(hrs*rate)
    elif hrs > 40:
        TotalPay=(40*rate) + (hrs-40)*1.5*rate

    print("Enter Hours:",hrs)
    print("Enter Rate:",rate)
    print ("Pay:",TotalPay)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()