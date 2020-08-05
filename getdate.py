import datetime
import calendar
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()] # E.g. Friday
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','Spetember',
                    'October','November','December']

    # A list of ordinal numbers
    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th',
                        '14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th',
                        '25th','26th','27th','28th','29th','30th','31st']

    return 'Today is ' + weekday + ', ' + ordinalNumbers[dayNum - 1] + ' of ' + month_names[monthNum - 1] + '.'
