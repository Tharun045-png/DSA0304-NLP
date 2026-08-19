machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

producing = []

for machine, status in machines.items():
    if status == "Active":
        producing.append(machine)
    elif status == "Maintenance":
        print(machine, "-> Not Producing")

print("\nProducing Machines:")
for machine in producing:
    print("Producing(" + machine + ")")