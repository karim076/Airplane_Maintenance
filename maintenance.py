import csv
import os
from datetime import datetime
from datetime import timedelta
#-----csv bestand openen en in een list of dicts plaatsen
maintenanceFile = open("maintenance.csv", "r")
reader = csv.DictReader(maintenanceFile)
maintenanceList = list(reader)
#------ Vars
today = datetime.now()
#-----While loop
isRunning = True
while isRunning:
    print("Welkom bij het onderhoudsboek!")
    print("1. Toon Vliegtuigen die in komende X maanden onderhoud nodig hebben")
    print("2. Toon het Y-aantal laatst onderhouden vliegtuigen")
    print("X. Afsluiten\n\n")
    answer = int(input("Maak uw keuze: "))
    os.system('cls')
    if answer == 1:
        month = int(input("Hoeveel maanden vooruit: "))
        month = month * 30
        check_date = today + timedelta(days=month)
        for plane in maintenanceList:
            plane['checkup_before'] = datetime.strptime(plane["checkup_before"], "%d/%m/%Y")
            if plane["checkup_before"] < check_date and plane['checkup_before'] > datetime.now():
                print(f"Plane id {plane['plane_id']} | Datum {plane['checkup_before']}")
    elif answer == 2:
        count = int(input("Hoeveel vliegtuigen tonen: "))
        data_sorted = sorted(maintenanceList, key=lambda row: datetime.strptime(row["last_checkup"], "%d/%m/%Y"), reverse=True)
        for i in range(count):
            item = data_sorted[i]
            print(f"plane id: {item['plane_id']} | Laatst gecheckt {item['last_checkup']}")
    elif answer.upper == "x":
        exit()
    else:
        os.system('cls')
        print("Probeer opnieuw")

    print("----------------------------")
    stop = input("Druk op enter om door te gaan of typ 'X'\n")
    os.system('cls')
    if stop.upper == "x":
        isRunning = False
    else:
        continue


#file dicht zetten
maintenanceFile.close