#This will be the main file, where all the functions are stored
import os
import openpyxl
import datetime
import json

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
    
Functions needed:
    VerifyJSON: Checks for existance, creates if not found. Returns the dict representing it
    VerifyXL:   Checks for existance, creates if not found. Returns the XL filename
    addTrip:    Collects all details required, appends them to JSON string
    deleteTrip: Allows the user to find and delete a specific trip
    editTrip    Allows the user to find and edit values from a specific trip
    recreateXL: Deletes and recreates the existing XL file found earlier, with updated data from the JSON dict
"""

def verifyJSON()->dict:
    delivery_data = {}
    current_time = datetime.datetime.now()
    year = current_time.year
    __filename__ = f"Delivery_Stats_{year}.Json"
    __filename__ = os.path.realpath(os.path.join(os.getcwd(), __filename__))
    print(f"{__filename__}")
    
    with open(__filename__, 'w+') as file:
        try:
            if (json.load(file) is not None):
                delivery_data = json.load(file)
        except:
            delivery_data = {}
    return (delivery_data)

def verifyXL()->str:
    current_time = datetime.datetime.now()
    year = current_time.year
    __filename__ = f"Delivery_Stats_{year}.Xlsx"
    __filename__ = os.path.realpath(os.path.join(os.getcwd(), __filename__))
    wb = openpyxl.Workbook()
    wb.save(__filename__)
    return(__filename__)

def addTrip():
    continue

def deleteTrip():
    continue

def editTrip():
    continue

def recreateXL():
    continue

def demo():
    print("Starting\n")
    verifyJSON()
    print("\ncompleted JSON\n")
    verifyXL()
    print("\ncompleted XLSX")

def main():
    demo()

if __name__ = "__main__":
    main()
