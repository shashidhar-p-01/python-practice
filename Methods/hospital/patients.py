def patient_info(name, age, ailment):
    return f"Name: {name}, Age: {age}, Ailment: {ailment}"

def calculate_medical_bill(days, rate):
    return days * rate

def is_critical(ailment):
    critical_ailments = ["heart attack", "stroke", "cancer"]
    return ailment.lower() in critical_ailments