#A config reader returns everything as strings: timeout = "30", retries = "3", verbose = "True". Convert each to the correct Python type. Watch the trap — bool("False") is not False.

timeout = "30"
retries = "3"
verbose = "True"
lis = [timeout,retries,verbose]
for i in range(0,len(lis)):
	if lis[i].isdigit():
		lis[i] = int (lis[i])
	elif lis[i] in ["True" , "False"]:
		if lis[i] == "True":
			lis[i] = True
		else:
			lis[i] = False

for i in lis:
	print(dtype(i))