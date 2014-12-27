
import os



response = os.system("ping c- 1 google.com")

if response == 0:
   print("Googles Down!")
else:
   print("Googles Up!")

