months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    old_date = input("Date: ").title().strip()

    for month in months:
        if old_date.startswith(month):
            if "," in old_date:
                if "/" not in old_date:
                    m = months.index(month) + 1
                    date_list = old_date.split()
                    d = int(date_list[1].replace(",", ""))
                    if d > 31:
                        continue
                    y = date_list[2]
                    print(f"{y}-{m:02}-{d:02}")
                    exit()

    if old_date.count("/") == 2:
        date_list = old_date.split("/")
        m, d, y = date_list
        d = int(d)
        if d > 31:
            continue
        try:
            m = int(m)
        except ValueError:
            continue
        if m > 12:
            continue
        print(f"{y}-{m:02}-{d:02}")
        break
