import csv
from filter import alternate_filter, filtered_shipments
with open("updated_shipments.csv") as shipments_file:
    reader = csv.DictReader(shipments_file)
    shipment_list = list(reader)
    june_shipments = alternate_filter(shipment_list, month="06")
    delivered_shipments = filtered_shipments(shipment_list, status="Delivered")

with open("june_shipments.csv", "w", newline="") as file_june:
    writer = csv.DictWriter(file_june, fieldnames=june_shipments[0].keys())
    writer.writeheader()
    writer.writerows(june_shipments)

with open("delivered.csv", "w", newline="") as file_delivered:
    writer = csv.DictWriter(file_delivered, fieldnames=delivered_shipments[0].keys())
    writer.writeheader()
    writer.writerows(delivered_shipments)