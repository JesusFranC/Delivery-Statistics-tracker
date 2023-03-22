#This will be the main
import os
from openpyxl import *
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

#

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
    VerifyJSON:
    VerifyXL:
    addTrip:
    deleteTrip:
    editTrip:
    recreateXL:
"""

def verifyJSON()->string:
    
