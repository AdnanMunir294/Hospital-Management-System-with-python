import pandas as pd
import numpy as np
import os
import time

class patient:
    def __init__(self, ID, Date, Disease, Medicine):
        self.ID = ID
        self.Date = Date
        self.Disease = Disease
        self.Medicine = Medicine

    def add_record(self):
        df_p = [self.ID, self.Date, self.Disease, self.Medicine]
        with open('data.txt','a') as datafile:
            datafile.write("\n")
            for data in df_p:
                datafile.write(str(data)+ " ")
        print("Record added successfully")
            
start = time.time()                
data = pd.read_csv("data.txt", sep=" ",names=["ID", "Date", "Disease", "Medicine"])
df = pd.DataFrame(data)
filename = str(input("Enter filename \t"))
if filename == "data":
    while (True):
        print("Welcome to Hope Medical Facility ")
        choice = int(input( "Choose your option: \n 1. Display the content of the file \n 2. Display all the records of the patients in the system \n \
3. Find a patient record at a date \n \
4. Find total number of visits of a patient \n \
5. Add a new Patient record \n \
6. Quit \n "))

        if choice == 1:
            print(data )
        elif choice == 3:
            ID = int(input("Please enter patient's ID \t"))
            a = df.loc[df['ID']== ID]
            a_dataframe = pd.DataFrame(a)
            if len(a) > 0:
                Date = str(input("Enter the date of visit in the form Month_date_Year"))
                find_Date = a_dataframe.loc[a_dataframe['Date'] == Date]
                if len(find_Date) > 0:
                    print("Patient Record :" )
                    print(find_Date.values.tolist())
                else:
                    
                   print(" No result against this Date \n")
            else:
                
                print(" No result found! \n")

        elif choice == 4:
            ID = int(input("Please enter patient's ID \t"))
            a = df.loc[df['ID']== ID]
            print("The total number of visits of patient" + str(ID) + " is:" + str(len(a)) + "\n")

        elif choice == 5:
            iid = str(input("Enter patient ID \t"))
            ddate = str(input("Enter the date of visit in the form Month_date_Year \t"))
            ddisease = str(input("Enter the reason of visit, separated by _ \t"))
            Mmedicine = str(input("Enter the treatment, separated by _  \t"))
            patient_new = patient(iid , ddate , ddisease , Mmedicine )
            patient.add_record(patient_new)

        elif choice==6:
            print("Thanks for visiting us")
            end = time.time()
            print("Excecution time: \t" + str (end - start))
            break
        
           
            
            





