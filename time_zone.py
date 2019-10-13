# class that handle the time zone and format transfer

# import library
from datetime import datetime
from dateutil import tz


# function that transfer GMT time zone to Melbourne time
def zone_change(time):

    from_zone = tz.gettz('GMT')
    to_zone = tz.gettz('Australia/Melbourne')
    utc = datetime.strptime(time, '%a, %d %b %Y %H:%M:%S %Z')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return (central.strftime( '%a, %d %b %Y %H:%M:%S %Z'))

if __name__ == '__main__':
    zone_change()
