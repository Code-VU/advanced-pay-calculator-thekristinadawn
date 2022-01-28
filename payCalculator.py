def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")

    try: 
        hrs=float(hrs)
    except: 
        print("Error, please enter numeric input.")
    rate = input("Enter Rate: ")
    try: 
        rate=float(rate)
    except: 
        print("Error, please enter numeric input.")
    if float(hrs) <=40:
        TotalPay=float(hrs*rate)
    elif float(hrs) > 40:
        TotalPay=float(rate*40) + float(hrs-40)*1.5*float(rate)
        print ("Pay:", TotalPay)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()