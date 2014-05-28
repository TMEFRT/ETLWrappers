#!/var/local/env-athena/bin/python
import os
import datetime
from datetime import timedelta

def prev_month_range(when = None):
    """Return (previous month's start date, previous month's end date)."""
    if not when:
        # Default to today.
        when = datetime.datetime.today()
    # Find previous month: http://stackoverflow.com/a/9725093/564514
    # Find today.
    first = datetime.date(day=1, month=when.month, year=when.year)
    # Use that to find the first day of this month.
    prev_month_end = first - datetime.timedelta(days=1)
    prev_month_start = datetime.date(day=1, month= prev_month_end.month, year= prev_month_end.year)
    # Return previous month's start and end dates in YY-MM-DD format.
    return (prev_month_start.strftime('%Y-%m-%d'), prev_month_end.strftime('%Y-%m-%d'))


month_dates = prev_month_range()

start_date = datetime.datetime.strptime(month_dates[0] , '%Y-%m-%d')
end_date = datetime.datetime.strptime(month_dates[1] , '%Y-%m-%d')

month_days = (end_date - start_date).days + 1

TEMP_FOLDER=os.getenv('TMP', '/tmp')

SF_FILE_NAME = '/date_file.txt'

try:

        DATES_FILE = open(TEMP_FOLDER + SF_FILE_NAME,'w')


        for i in range(0,month_days):
                DATES_FILE.write((start_date + timedelta(days=i)).strftime('%Y-%m-%d') + '\n')

except Exception, e:
        print "Check Exception" + str(e)

finally:
        DATES_FILE.close()
