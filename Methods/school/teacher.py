def teacher(name, subject):
    return f"{name} teaches {subject}"  


def calculate_salary(hours, rate):
    return hours * rate


def is_eligible_for_bonus(salary, performance):
    if performance == "excellent":
        return salary * 0.1
    elif performance == "good":
        return salary * 0.05
    else:
        return 0