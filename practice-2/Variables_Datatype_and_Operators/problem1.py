#A health check script reads CPU usage from a log as the string "87.5". Convert it to a float, check if it's above 80, and print: "ALERT: web01 CPU at 87.5% — threshold breached" using an #f-string.

cpu_usage = "87.5"
cpu_usage_float = float(cpu_usage)
if cpu_usage_float > 80:
	print(f"ALERT: web01 CPU at {cpu_usage_float}% -- threshold breached")