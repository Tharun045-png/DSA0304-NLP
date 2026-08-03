words = ["writes", "writing", "written"]

print("{:<12}{:<25}{:<12}{:<10}{:<12}".format(
    "Word","State Path","Pattern","Root","Normalized"))

for word in words:

    if word == "writes":
        path = "Start->write->s->Final"
        pattern = "Regular"

    elif word == "writing":
        path = "Start->write->ing->Final"
        pattern = "Regular"

    elif word == "written":
        path = "Start->write->en->Final"
        pattern = "Irregular"

    print("{:<12}{:<25}{:<12}{:<10}{:<12}".format(
        word,path,pattern,"write","write"))