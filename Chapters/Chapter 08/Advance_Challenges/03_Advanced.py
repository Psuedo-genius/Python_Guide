# Loop to display a countdown with delay (optional `time.sleep`)
import time  # Import the time module
# Its the use of mudule to introduce a delay between each countdown
countdown = 10
delay = 1  # Delay in seconds

while countdown > 0:
    print(countdown)
    time.sleep(delay)  # This adds the delay
    countdown -= 1

print("Countdown finished!")
# or
# we con leave the optional part
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Countdown finished!")
