def salary(a):
    if a == "manager":
        return 5000
    elif a == "developer":
        return 4000
    else:
        return 3000


def bonus(a,b):
    if b == "good":
        return a + 500
    elif b == "average":
        return a + 200
    else:
        return a