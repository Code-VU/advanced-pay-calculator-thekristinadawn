def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    pay = float(rate)
    if h <=40:
        TotalPay=(h*pay)
    elif h > 40:
        TotalPay=(40*pay) + (h-40)*1.5*pay

    print("Enter Hours:" +" "+ hrs)
    print("Enter Rate:" +" "+ rate)
    print ("Pay:" , TotalPay)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()