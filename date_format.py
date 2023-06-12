from datetime import datetime

def datetime_format(orig_str):
    date_object = datetime.strptime(orig_str, "%B%d%Y")
    date_format = date_object.strftime("%Y%m%d")
    return date_format

if __name__ == "__main__":
    print(str(datetime_format('April12023'))) # => '20230401'