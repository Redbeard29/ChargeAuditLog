import json

charges_list = []

file = open('data.json',)
chargesAsDict = json.load(file)

for charge in chargesAsDict:
    charges_list.append(charge)
print(charges_list)

test_dict = {
    "id": 3,
    "chargeName": "corn",
    "chargeDate": "January 1st, 2022",
    "initialCost": 3.00,
    "remainingCost": 2.50,
    "isPaid": False
}

json_object = json.dumps(test_dict, indent=4)

with open("data.json", "w") as outfile:
    outfile.write(json_object)