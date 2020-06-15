# ALERT BOTH MAX AND MIN BATTERY...
    
import psutil, time
from pygame import mixer 

i = 0
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

maxbat = 97
minbat = 30

if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"

status = str(percent) + '% | ' + plugged
print(status)

count = 0
data = []

while True:

    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
        
    count += 1
    i += 1
    data.append(percent)

    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', plugged, str(battery))
    time.sleep(3)

    if percent >= maxbat or percent <= minbat:
        
        mixer.init()
        mixer.music.load('gajban.mp3') 
        mixer.music.set_volume(0.9) 
        mixer.music.play() 

        input('\nPRESS => ENTER to stop Alarm and CHANGE CHARGING PLUG STATUS : ')
        mixer.music.stop()
        
        print("\nWaiting for 60 seconds...\n")
        time.sleep(60)
        continue

    else:
        continue
    