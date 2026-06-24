import os
import csv
from datetime import date

# Implement the actual saving process here.
def edit_password(platform, password, old_platform, old_password):
    file = "passSave.csv"
    newPasswordList = []

    if os.path.exists(file):
        with open(file, "r", newline='') as fileR:
            csv_reader = csv.reader(fileR)
            for i in csv_reader:
                if (i[0] != old_platform and i[1] != old_password):
                    newPasswordList.append(i)
                else:
                    dateString = str(date.today())
                    newPasswordList.append([platform, password, dateString])

        with open(file, "w", newline='') as fileW:
            writer = csv.writer(fileW)
            writer.writerows(newPasswordList)