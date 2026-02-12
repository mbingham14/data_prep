import re
import matplotlib.pyplot as plt


fname = "mbox.txt"

days = []
months = []

with open(fname, "r") as f:
    for line in f:
        match = re.search(r'^From\s+\S+\s+(\w{3})\s+(\w{3})\s+\d+\s+\d+:\d+:\d+\s+\d{4}', line)

        if match:
            days.append(match.group(1))
            months.append(match.group(2))

# (a) Histogram: emails by month
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month_values = []
for m in month_order:
    month_values.append(months.count(m))

plt.figure()
plt.bar(month_order, month_values, width=0.6)
plt.xlabel('Month')
plt.ylabel('Number of Emails')
plt.title('Emails Sent by Month')


# (b) Histogram: emails by day of week
day_order = ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun']
day_values = []
for d in day_order:
    day_values.append(days.count(d))

plt.figure()
plt.bar(day_order, day_values, width=0.6)
plt.xlabel("Day of Week")
plt.ylabel("Number of Emails")
plt.title("Emails Sent by Day of Week")
plt.show()
