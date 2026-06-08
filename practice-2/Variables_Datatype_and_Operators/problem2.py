#You have disk_used = 450 and disk_total = 500. Calculate the percentage using arithmetic operators, round to 2 decimal places, and print "CRITICAL" if above 90%, "WARNING" if above 75%, else #"OK".

disk_used = 450
disk_total = 500
disk_used_percentage = round((disk_used/disk_total)*100,2)
print(f"CPU usage : {disk_used_percentage}%")
if disk_used_percentage > 90 :
	print("CRITICAL")
elif disk_used_percentage > 75 :
	print("WARNING")
else:
	print("OK")