from datetime import datetime

def date_format(date_input):
    date = datetime.strptime(date_input, "%Y%b%d")
    date_format = date.strftime("%d/%m/%Y")
    return date_format

print(date_format("2023Jan1"))