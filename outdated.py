
months = [

    "January", "February", "March", "April", "May", "June",

    "July", "August", "September", "October", "November", "December"

]


while True:
    date = input("Date: ").strip()

    try:

        if "/" in date:
            parts = date.split("/")

            if len(parts) != 3:
                raise ValueError

            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

        else:

            if "," not in date:
                raise ValueError

            month_part, rest = date.split(" ", 1)

            if month_part.capitalize() not in months:
                raise ValueError

            rest_parts = rest.split(",")
            if len(rest_parts) != 2:

                raise ValueError


            day_str = rest_parts[0].strip()
            year_str = rest_parts[1].strip()

            day = int(day_str)
            year = int(year_str)

            if not (1 <= day <= 31):
                raise ValueError

            month = months.index(month_part.capitalize()) + 1

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except:
        continue
