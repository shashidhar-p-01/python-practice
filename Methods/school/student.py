def student_info(name, age, grade):
    return f"Name: {name}, Age: {age}, Grade: {grade}"

def calculate_gpa(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)
    
def is_passing(grade):
    return grade >= 60
