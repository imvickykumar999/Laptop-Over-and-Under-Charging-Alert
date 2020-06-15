import psutil, time, winsound

maxbat, minbat = 95, 30

frequency = 2500
duration = 1000

count = 1
while True:

    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
    
    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', str(battery))
    time.sleep(60)
    count += 1

    if percent >= maxbat or percent <= minbat:
    
        for i in range(10):
            winsound.Beep(frequency, duration)
            time.sleep(.5)
            
        print('\nRemove Charging Plug...\n')   
        time.sleep(150)