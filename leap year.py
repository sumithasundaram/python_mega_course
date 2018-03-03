def leap_year(x):
    if(x % 4 == 0):
        print("The year is a leap year")
    else:
        print("The year is a not leap year")
if __name__=="__main__":
    year=int(input('enter the year:'))
    leap_year(year)
