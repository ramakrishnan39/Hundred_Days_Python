# craete function is_leap()
# create function days_in_month(year, month)

def is_Leap(year):
    if year % 4 == 0 :
        if year % 100 ==0 :
            if year % 400 ==0:
                return True
            return False
        return True
    return False

def days_in_month(yr,mnth):
    d31=["January","March","May","July","August","October","December","1","3","5","7","8","10","12"]
    d30=["April","June","September","November","4","6","9","11"]
    dleap=["February","2"]
    if mnth in d31:
        print("31")
    elif mnth in d30:
        print("30")
    elif mnth in dleap:
        if is_Leap(yr):
            print("29")
        else:
            print("28")
    else:
        print("Enter the valid month name to check")

days_in_month(int(input("Enter the year ")), input("Enter the month "))