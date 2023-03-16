#Test File meant to show how to create, print the name, and delete files
import os
import openpyxl

__file__ = "test"
__file__ = __location__ = os.path.realpath(os.path.join(os.getcwd(), __file__))

wb = openpyxl.Workbook()
wb.save(__file__+".xlsx")

print(__file__)


wb2 = openpyxl.load_workbook(__file__+  ".xlsx")
wb2.save(__file__+"2.xlsx")

input("press enter to continue:")

os.remove(__file__+"2.xlsx")
os.remove(__file__+".xlsx")
