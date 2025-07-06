import csv
from loads import shipments
fields = ["LoadNum", "ActivityDate", "Origin", "Destination", "Status", "ApptNum", "DeliveryDate"]

with open("updated_shipments.csv", "w", newline="") as updated_shipments:
    load_list = csv.DictWriter(updated_shipments, fieldnames=fields)
    load_list.writeheader()
    for loads in shipments:
        loads["ApptNum"] = "N/A"
        loads["DeliveryDate"] = "TBD"
        load_list.writerow(loads)
