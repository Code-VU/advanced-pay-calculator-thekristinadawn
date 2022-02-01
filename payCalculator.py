def calculatePay():
    
    # This first line is provided for you
    try: 
    	hrs=input("Enter Hours:")
        hrs_float=float(hrs)
        rate = input("Enter Rate:")
        rate_float=float(rate)
          
    except: 
        print("Error, please enter numeric input.")

    if hrs_float<=40:
        RegPay = hrs_float*rate_float
        print("Pay:",RegPay)
    else:
        RegOtPay = rate_float*40 + (hrs_float-40)*1.5*rate_float
        print ("Pay:",RegOtPay)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()