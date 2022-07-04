from babel import dates
import datetime
from random import randint

d = datetime.datetime.today() + datetime.timedelta(days=randint(1,30))
form = dates.format_datetime(d, "EEEE d MMMM yyyy",locale='pl_PL')
print(form)