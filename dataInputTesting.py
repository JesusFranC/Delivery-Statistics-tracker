import os
import openpyxl
import datetime

def demo():
    current_time = datetime.datetime.now()
    month = current_time.month
    day = current_time.day
    year = current_time.year
    hour = current_time.hour
    minute = current_time.minute
    if minute < 10:
        minute = "0" + str(minute)
    if hour < 12:
        if hour == 0:
            hour = 12
        print(f"{month}/{day}/{year} {hour}:{minute}AM")
    else:
        print(f"{month}/{day}/{year} {hour}:{minute}PM")

def main():
    print ("Good evening!")
    demo()
    
if __name__ == "__main__":
    main()
