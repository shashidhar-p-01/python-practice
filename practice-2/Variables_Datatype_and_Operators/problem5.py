#Given uptime_seconds = 345678, use only arithmetic operators to break it into days, hours, and minutes. Print: "Uptime: 3d 23h 59m".

uptime_seconds = 345678
uptime_minutes = uptime_seconds//60
uptime_hours = uptime_minutes//60
uptime_minutes = uptime_minutes%60
uptime_days = uptime_hours//24
uptime_hours = uptime_hours%24

print(f"Uptime: {uptime_days}d {uptime_hours}h {uptime_minutes}m")