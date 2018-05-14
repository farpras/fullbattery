from win10toast import ToastNotifier
import psutil
import time

def fullBattery():
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = battery.percent
	if plugged and percent >= 99:
		plugged = "Plugged in"
		toaster = ToastNotifier()
		toaster.show_toast(
			"Fully Charged!",
			"Battery is fully charged. Please unplug the charger!",
			icon_path = "icon.ico",
			duration = 10,
			threaded = True
			)
	else:
		plugged = "Unplugged"
	print('Status: ' + str(percent) + '% (' + plugged + ')\nLaunched notification test!')
	time.sleep(300)

while True:
	fullBattery()