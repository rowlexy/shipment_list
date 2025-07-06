from loads import shipments
 
def filtered_shipments(shipments, load_num=None, month=None, pu_date=None, origin=None, status=None, consignee=None):
    load_results = []
    for loads in shipments:
        if (pu_date and loads["ActivityDate"] != pu_date):
            continue
        if (month and loads["ActivityDate"].split("-")[1] != month):
            continue
        if (origin and loads["Origin"] != origin):
            continue
        if (load_num and loads["LoadNum"] != load_num):
            continue
        if (status and loads["Status"] != status):
            continue
        if (consignee and loads["Destination"] != consignee):
            continue
        # if (loads["DeliveryDate"] and del_date != del_date):
        #     continue
        # if (loads["ApptNum"] and appt_num != appt_num):
        #     continue
        load_results.append(loads)
    return load_results

# for loads in filtered_shipments(shipments, status="Delivered"):
#     print(loads)
    
def alternate_filter(shipments, **param):
    load_results = []
    for loads in shipments:
        match = True
        for key, value in param.items():
            if key == "month":
              if loads["ActivityDate"].split("-")[1] != value:
                match = False
                break
            elif loads.get(key) != value:
                match = False
                break
        if match:
            load_results.append(loads)
    return load_results

print('\n Shipments Collected In June \n')
for loads in alternate_filter(shipments, month="06"):
    print(loads)
for loads in alternate_filter(shipments, status="Delivered"):
    print(loads)