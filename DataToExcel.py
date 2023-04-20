#This will be the main file, where all the functions are stored
import os
import openpyxl
import datetime
from datetime import date
import json

#######################################################
#NEED TO ADD FEATURE TO ENSURE TRIPS ARENT ADDED TWICE#
#######################################################

#first, we initialize and make sure that the Excel file exists
    #We create if not existing, and we return if it does
    #The filename is "Delivery_Stats_{Year}.XLSX"
#Second, We initialize and make sure that a JSON file exists
    #We create it if it does not exist, then return it once its there
    #The filename is "Delivery_Stats_{Year}.JSON"

#We then start a gui asking what we would like to do
    #(Current options would only be to add, remove or edit a trip)
    #all functions will be added, and all changes will be made to the JSON String.
    #The JSON is constantly saved, after each and every option is finished running

#All changes are finished as soon as we are done running commands at the end of the program.
#Before the program finsishes running, it will lastly wipe and recreate the XLSX File, as a new updated version
    #It does this using the information from the JSON File, Reading and updating all row by row
    #All info will be sorted by date

"""
Variables to be collected:
    Date:       MM/DD/YYYY
    Time:       HR:Min
    Duration:   Time taken in minutes
    Start Zip:  Zipcode where the trip started
    End Zip:    Zipcode where the trip ended
    Distance:   Distance driven in miles
    Service:    Service Uses, such as Delivery, package, GoPuff, McDonalds, and Prop 22
    Tip:        Tip Pay given by client
    BasePay:    Base Pay given by Uber

json format:
    
Main Functions needed:
    VerifyJSON: Checks for existance, creates if not found. Returns the dict representing it
    VerifyXL:   Checks for existance, creates if not found. Returns the XL filename
    addTrip:    Collects all details required, appends them to JSON string
    deleteTrip: Allows the user to find and delete a specific trip
    editTrip    Allows the user to find and edit values from a specific trip
    recreateXL: Deletes and recreates the existing XL file found earlier, with updated data from the JSON list
    updateJSON: Updates all data in the JSON file
Supporting Functions needed:
    checkMonth: Ensures we select a valid month
    checkDay:   Ensures we select a valid day for the given month
    checkTIme:  Ensures we select a valid 24hr time in HH:MM format
    tripFinder: Finds a valid trip, returns the index from the "data" list
"""

def checkMonth()->int:
    flag = False
    month = 0
    print("What month were/was the deliveries/delivery?")
    while flag is not True:
        try:
            month = int(input("Please enter a number from 1 to 12\n"))
            if month < 1 or month > 12:
                print("---Not a valid month---")
            else:
                check = input(f"Is the following month correct: {month}\nPlease enter Yes or No\n")
                check = check.lower()
                if check == "yes":
                    flag = True
        except:
            continue
    return month

def checkDay(month: int, year: int)->int:
    lastDay = 0
    if month == 12:
        lastDay = abs((date(year, 12, 1) - date(year+1, 1, 1)).days)
    else:
        lastDay = abs((date(year, month, 1) - date(year, month+1, 1)).days)
    flag = False
    day = 0
    print("What day were/was the deliveries/delivery?")
    while flag is not True:
        try:
            day = int(input(f"Please enter a number from 1 to {lastDay}\n"))
            if day < 1 or day > lastDay:
                print("---Not a valid day---")
            else:
                check = input(f"Is the following day correct: {day}\nPlease enter Yes or No\n")
                check = check.lower()
                if check == "yes":
                    flag = True
        except:
            continue
    return day

#will return a valid 24hr time in HH:MM format, as a string
def checkTime()->str:
    validTime = ""
    flag = False
    while flag == False:
        try:
            time = input("please enter the time as a 24 hour time in HH:MM format (ie: 13:52)\n")
            timeformat = "%H:%M"
            datetime.datetime.strptime(time, timeformat)
            validTime = time
            flag = True
        except:
            print("invalid time")
            continue
    return validTime

"""
data:   List of all trips
year:   Year trips take place

Returns the index from data, for a specific trip to be affected from a given day. Returns -1 if no trip found on that day
"""
def tripFinder(data, year)->int:
    month = checkMonth()
    day = checkDay(month, year)
    date = datetime.datetime(year, month, day)  #I am creating a date time object
    dateString = date.strftime("%m/%d/%Y")      #I am converting the date time object to a string
    dateMatchIndex = []                         #I will hold the list of indexes where the date matches here
    matchNum = 0                                #The number of matching date trips
    for i in range(len(data)):  #scans through and gets trips on given day
        if data[i]['date'] == dateString:
            dateMatchIndex.append(i)
            matchNum = matchNum + 1
    if matchNum > 0:    #"if there were any trips this day"
        print("These are all times for each trip this day:")
        for i in range(len(dateMatchIndex)):    #Gets the times for each trip on given day
            trip = i+1
            print(f"Trip {trip}: {data[dateMatchIndex[i]]['time']}")
        while True:     #this loop ensures that a valid trip is selected
            try:
                trip = int(input(f"What trip would you like to select?\nEnter a number from 1 to {len(dateMatchIndex)}: "))
                return dateMatchIndex[trip-1]
            except:
                print("Trip Finder has broken")
                continue
    else:   #If there were no trips this day
        print("No matches for this day!")
        return -1

def tripDetails(data: list, index: int):
    
    for key in data[index].keys():
        
        print(f"{key}: {data[index][key]}")
    

def verifyJSON(year)->list:
    delivery_data = []
    __filename__ = f"Delivery_Stats_{year}.Json"
    __filename__ = os.path.realpath(os.path.join(os.getcwd(), __filename__))
    #print(f"{__filename__}")

    with open(__filename__, 'r') as file:
        try:
            print("About to load")
            tempData = json.load(file)
            if tempData is not None:
                print("Loading Existing File\n")
                delivery_data = tempData
        except:
            print("Creating Blank Data\n")
            delivery_data = []
    return (delivery_data)

def verifyXL()->str:
    current_time = datetime.datetime.now()
    year = current_time.year
    __filename__ = f"Delivery_Stats_{year}.Xlsx"
    __filename__ = os.path.realpath(os.path.join(os.getcwd(), __filename__))
    wb = openpyxl.Workbook()
    wb.save(__filename__)
    return(__filename__)

def addTrip(data: list, year)->None:
    #Date:       MM/DD/YYYY
    month = checkMonth()
    day = checkDay(month, year)
    date = datetime.datetime(year, month, day)  #I am creating a date time object
    dateString = date.strftime("%m/%d/%Y")      #I am converting the date time object to a string
    
    trips = 0
    while True:
        try:
            trips= int(input("How many trips were made this day?\n"))
            break
        except:
            continue

    for i in range(trips):
        currentTrip = i+1
        print(f"---For trip {currentTrip}---")
        #Time:       HR:Min
        timeString = checkTime()
        #Duration:   Time taken in minutes
        duration = input("How long did the trip take in minutes?\n")
        #Start Zip:  Zipcode where the trip started
        startZip = input("What zipcode did the trip start in?\n")
        #End Zip:    Zipcode where the trip ended
        endZip = input("What zipcode did the trip end at?\n")
        #Distance:   Distance driven in miles
        distance = input("How many miles were driven?\n")
        #Service:    Service Uses, such as Delivery, package, GoPuff, McDonalds, and Prop 22
        service = input("What service was used?\n")
        #Tip:        Tip Pay given by client
        tip = input("what was the tip given?\n")
        #BasePay:    Base Pay given by Uber
        basePay = input("What was the base pay for the trip?\n")
        newTrip = {'date': dateString,'time':timeString,'duration':duration,'sZip':startZip,'eZip':endZip,'distance':distance,'service':service,'tip':tip,'base':basePay}
        data.append(newTrip)
    return

def deleteTrip(data, year):
    tripID = tripFinder(data, year)
    trip = data.pop(tripID)
    print(f"Trip on {trip[date]} at {trip[time]} has been deleted")
    return

def editTrip():
    
    return

def recreateXL():
    return

def updateJSON(data, year):
    __filename__ = f"Delivery_Stats_{year}.Json"
    __filename__ = os.path.realpath(os.path.join(os.getcwd(), __filename__))
    with open(__filename__, 'w+') as outfile:
        try:
            json.dump(data, outfile)
        except:
            print("The upload has failed, JSON could not be updated")
    return

def demo():
    ###OLD DEMO CODE
##    current_time = datetime.datetime.now()
##    year = current_time.year
##    data = verifyJSON(year)
##    print(data)
##    addTrip(data, year)
##    for info in data:
##        print(info)
##    updateJSON(data, year)
##    trip = tripFinder(data, year)
    #Current functional GUI
    current_time = datetime.datetime.now()
    year = current_time.year
    data = verifyJSON(year)
    userIn = ""
    while True:
        try:
            userIn = int(input("What would you like to choose?\n1: Add trip\n2: Delete Trip\n3: Edit Trip\n4: Trip Details\n5: Quit\n"))
            if userIn == 1:
                addTrip(data, year)
            elif userIn == 2:
                deleteTrip(data, year)
            elif userIn == 3:
                editTrip(data, year)
            elif userIn == 4:
                tripID = tripFinder(data, year)
                if tripID != -1:
                    tripDetails(data, tripID)
            elif userIn == 5:
                break
            else:
                print("Please enter a valid choice!")
        except:
            print("That was not a number!")
        
    
def main():
    demo()

if __name__ == "__main__":
    main()
