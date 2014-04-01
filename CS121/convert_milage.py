def convert_mileage(x):
    mpg = x
    #set y to be gallons/liters
    y = 3.78541178
    #Convert KM
    x = x * 1.609344
    #get Liters per KM
    x = y/x
    #get liters per 100KM
    x = x*100
    print(str(mpg) + 'MPG converted to L/100KM is:')
    print round(x,2)
    return

#Convert 40 mpg to L/100KM
convert_mileage(40)

#convert 20 mpg to L/100KM
convert_mileage(20)