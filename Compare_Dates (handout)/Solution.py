from datetime import datetime
date1 =input()
date2 = input()


def compare_dates(date1, date2):
    format = "%d/%m/%Y"

    #
    try:
        d1 = datetime.strptime(date1, format)
    except ValueError:
        return f"Invalid date {date1}"


    try:
        d2 = datetime.strptime(date2, format)
    except ValueError:
        return f"Invalid date {date2}"

   
    if d1 < d2:
        return -1
    elif d1 > d2:
        return 1
    else:
        return 0

    
print(compare_dates(date1, date2))