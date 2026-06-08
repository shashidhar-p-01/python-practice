#A hostname comes in from user input as " Web-Server-01 ". Clean it to "web-server-01" using string methods only — no manual loops.

hostname = " Web-Server-01 "
hostname = hostname.strip()
hostname = hostname.lower()
print(hostname)