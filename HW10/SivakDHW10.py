from datetime import datetime

date_input = "Feb 12 2019 2:41PM"
date_output = str(datetime.strptime(date_input, "%b %d %Y %I:%M%p"))

print(date_output)