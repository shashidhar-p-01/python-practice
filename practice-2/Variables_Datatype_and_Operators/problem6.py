#You need to validate a port number entered as a string. Check it's numeric, convert to int, and verify it's between 1 and 65535. Print "VALID" or "INVALID" with a reason.

port_number = input("Enter port number : ")


if port_number.isdigit():
	port_number = int(port_number)

if 1 <= port_number <= 65535 :
	print("VALID port number")
else:
	print("INVALID : the port number must be in the range 1 and 65535")

