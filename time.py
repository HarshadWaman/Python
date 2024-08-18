# get system date and time 
from datetime import datetime
x=datetime.now()

y=x.strftime("%H:%M%p")
z=x.hour

print("Hello!")
if 6 <= z <12:
    print("Good moring sir.")
elif 12 <= z <17:
    print("Good afternoon sir.")
elif 17 <= z <18:
    print("Good evening sir.")
else:
    print("Good night sir.")
    
print("your currant date and time is:",x)
