import psutil
import urllib.request


def get_system_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    if battery:
        battery_percent = battery.percent
        charging = battery.power_plugged

        if charging:
            battery_status = f"{battery_percent}% and charging"
        else:
            battery_status = f"{battery_percent}%"

    else:
        battery_status = "Battery information unavailable"

    return (
        f"CPU usage is {cpu}%. "
        f"RAM usage is {ram}%. "
        f"Battery is {battery_status}."
    )


def get_battery_status():
    battery = psutil.sensors_battery()

    if not battery:
        return "Battery information unavailable."

    if battery.power_plugged:
        return f"Battery is {battery.percent}% and charging."

    return f"Battery is {battery.percent}%."


def check_internet():
    try:
        urllib.request.urlopen(
            "https://www.google.com",
            timeout=5
        )
        return True

    except Exception:
        return False