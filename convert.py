import csv

if __name__ == "__main__":
    with open("./Visacard BusinessCard Goldkart.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        months = {}

        for row in reader:
            day, month, year = row["Date"].split(".")
            currency = row["Currency"]
            amount = row["Amount"]
            description = row["Name"] + " " + row["Purpose"]

            monthkey = f"{year}-{month}"
            data = {
                "Währung": currency,
                "VorzBetrag": amount,
                "RechNr": "",
                "BelegDatum": f"{day}{month}",
                "Belegtext": description,
                "UStSatz": "",
                "BU": "",
                "Gegenkonto": "",
                "Kost1": "",
                "Kost2": "",
                "Kostmenge": "",
                "Skonto": "",
                "Nachricht": "",
            }
            if monthkey in months:
                months[monthkey] += [data]
            else:
                months[monthkey] = [data]

    for monthkey, data in months.items():
        with open(f"./datevcsvout/{monthkey}.csv", "w", newline="") as csvfile:
            fieldnames = [
                "Währung",
                "VorzBetrag",
                "RechNr",
                "BelegDatum",
                "Belegtext",
                "UStSatz",
                "BU",
                "Gegenkonto",
                "Kost1",
                "Kost2",
                "Kostmenge",
                "Skonto",
                "Nachricht",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()

            for row in data:
                writer.writerow(row)
