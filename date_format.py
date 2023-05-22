# 'February42020' => '20200204'
# 'April32018' => '20180403'
# 'October252022' => '20221025'

"""
without module
"""

"""
{"February":"02", "April":"04", "October":"10"}
"""

def date_format(orig_str):
    year = orig_str[-4:]
    try: 
        date = str(int(orig_str[-6:-4]))
        month = orig_str[:-6]
    except:
        date = "0"+orig_str[-5]
        month = orig_str[:-5]
    
    month_dict = {"February":"02", "April":"04", "October":"10"}
    month = month_dict.get(month)
    

    return year + month + date

print(date_format('February252020')) # => '20200204'