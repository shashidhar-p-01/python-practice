def doctors_info(name, specialization, experience):
    return f"Name: {name}, Specialization: {specialization}, Experience: {experience} years"

def calculate_consultation_fee(specialization, experience):
    base_fee = 100
    if specialization.lower() == "cardiologist":
        base_fee += 50
    elif specialization.lower() == "neurologist":
        base_fee += 40
    elif specialization.lower() == "general practitioner":
        base_fee += 20
    
    experience_bonus = experience * 10
    return base_fee + experience_bonus

def is_available(working_hours, current_time):
    start_time, end_time = working_hours
    return start_time <= current_time <= end_time

