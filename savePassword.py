import os
from datetime import date

# Implement the actual saving process here.
def save_password(platform, password):
    file = "passSave.csv"

    if os.path.exists(file):
        fileA = open(file, "a")
        fileA.write(f"{platform},{password},{date.today()}\n")

        fileA.close()
    else:
        fileW = open(file, "w")
        fileW.write(f"{platform},{password},{date.today()}\n")

        fileW.close()