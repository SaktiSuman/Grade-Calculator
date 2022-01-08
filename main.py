sakti = {"name": "Sakti Suman",
         "assignment": [80, 50, 40, 20],
         "test": [75, 75],
         "lab": [78.20, 77.20]
         }

akash = {"name": "Akash Mohanty",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

bithal = {"name": "Bithal Pattnaik",
          "assignment": [77, 82, 23, 39],
          "test": [78, 77],
          "lab": [80, 80]
          }

sumit = {"name": "Sumit Pradhan",
         "assignment": [67, 55, 77, 21],
         "test": [40, 50],
         "lab": [69, 44.56]
         }


def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


def calculate_total_average(student):
    assignment = get_average(student["assignment"])
    test = get_average(student["test"])
    lab = get_average(student["lab"])
    # Return the result based
    # on weightage supplied
    # 20 % from assignments
    # 80 % from test
    # 30 % from lab-works
    return (0.2 * assignment + 0.8 * test + 0.3 * lab)


def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


def class_average(student_list):
    result_list = []
    for student in students_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
    return get_average(result_list)


students_list = [sakti, akash, bithal, sumit]
for i in students_list:
    print(f"The average mark of {i['name']} is {calculate_total_average(i)}")
    print(f"The letter grade of {i['name']} is {assign_letter_grade(calculate_total_average(i))}")
    print("\r")

class_av = round(class_average(students_list), 2)
print(f"The average of the class is {class_av}")
