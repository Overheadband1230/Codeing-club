import subprocess
import time
print("Welcome to Python Cash handler")
print("Please wait while program boots")
time.sleep(10)

print("Program Boot is successful")
print("please login when prompted")
time.sleep(4)
subprocess.run(["python", "login.py"])
