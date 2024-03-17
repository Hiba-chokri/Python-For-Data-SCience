import datetime
time = datetime.datetime(1970,1,1)
N_time = datetime.datetime.now() - time
seconds = (N_time.total_seconds())
print("Seconds since January 1, 1970 :",f'{seconds:,.6f}', "or", format(seconds, ".1E"), "in scientific notation")
date = datetime.datetime.now()
print(date.strftime("%b %d %Y"))