def calculatePay():
    
    # This first line is provided for you
    hrs=input("Enter Hours: ") 
    
    try: 
        float(hrs)
        try:
            rate = input("Enter Rate: ")
            float(rate)
            if float(hrs)>40:
                RegOtPay = float(rate)*40 + (float(hrs)-40)*1.5*float(rate)
                pay = RegOtPay
            else:
                pay = float(hrs)*float(rate)   
            print ("Pay:",pay)
        except: 
            print("Error, please enter numeric input")
    except: 
        print("Error, please enter numeric input")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()