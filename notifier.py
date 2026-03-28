import psutil
import time
from plyer import notification
import winsound

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        
        if battery:
            percent = battery.percent
            plugged = battery.power_plugged
            
            if plugged and percent >= 75:
                # Play the default Windows notification sound
                # (You can also use a custom .wav file: winsound.PlaySound("your_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC))
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)

                notification.notify(
                    title="Battery Alert 🔋",
                    message=f"Battery is at {percent}%. You can unplug now!",
                    timeout=10  # notification stays for 10 seconds
                )
                print(f"Notification sent! Battery: {percent}%")
                time.sleep(3600)  # wait 1 hour before checking again
            else:
                print(f"Battery: {percent}% | Plugged: {plugged}")
        
        time.sleep(60)  # check every 60 seconds

if __name__ == "__main__":
    print("Battery monitor started...")
    check_battery()