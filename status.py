import csv
import smtplib
from filter import alternate_filter, filtered_shipments
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")
recipient = os.getenv("RECIPIENT_LIST")
recipient_list = recipient.split(",")


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

# Build the email content   
email_content = "Please find report for the month of June in the attached file\n\n"
message = EmailMessage()
message.set_content(email_content)
message["Subject"] = "June Deliveries Report"
message["From"] = email_user
message["To"] = ", ".join(recipient_list)

for report in ["june_shipments.csv", "delivered.csv"]:
    with open(report, "rb") as f:
        message.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=report)
# Compose email

# Adding files as attachement


# Send email via SMTP
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_user, email_pass)
    smtp.send_message(message)
