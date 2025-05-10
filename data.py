import calendar 

yy = 2025
mm = 1

for i in range(12):
    mm = i + 1 
    print(calendar.month(yy,mm))
    