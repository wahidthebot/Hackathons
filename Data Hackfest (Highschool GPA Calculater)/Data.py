# Function to check if the input grade is in bounds
def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("Invalid input. Please enter a GPA between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 0.0 and 4.0.")

# Inputs
print("Enter your grades as a GPA out of 4.0\n")

# 9th grade inputs
ninth_grade_math = get_valid_grade("What was your grade for Math in 9th grade: ")
ninth_grade_ela = get_valid_grade("What was your grade for ELA in 9th grade: ")
ninth_grade_history = get_valid_grade("What was your grade for History in 9th grade: ")
ninth_grade_science = get_valid_grade("What was your grade for Science in 9th grade: ")

# Collect 9th-grade extracurricular activities and grades
extra_curriculars_ninth_grade = []
num_extra = int(input("\nHow many extracurriculars did you do in 9th grade: "))

for i in range(num_extra):
    activity = input(f"Enter the name of extracurricular activity {i + 1}: ")
    grade = float(input(f"Enter the grade for {activity} in 9th grade: "))
    extra_curriculars_ninth_grade.append((activity, grade))

# Calculate the extracurricular GPA
extracurricular_grades = [grade for (_, grade) in extra_curriculars_ninth_grade]
extracurricular_gpa = sum(extracurricular_grades) / len(extracurricular_grades)

# Calculate the main GPA for 9th grade
ninth_grade = [ninth_grade_math, ninth_grade_ela, ninth_grade_history, ninth_grade_science]
ninth_grade_gpa = (sum(ninth_grade) + extracurricular_gpa) / (len(ninth_grade) + 1)

print(f"\nYour 9th Grade GPA was: {ninth_grade_gpa:.2f}\n")

# 10th grade inputs
tenth_grade_math = get_valid_grade("What was your grade for Math in 10th grade: ")
tenth_grade_ela = get_valid_grade("What was your grade for ELA in 10th grade: ")
tenth_grade_history = get_valid_grade("What was your grade for History in 10th grade: ")
tenth_grade_science = get_valid_grade("What was your grade for Science in 10th grade: ")

# Collect 10th-grade extracurricular activities and grades
extra_curriculars_tenth_grade = []
num_extra = int(input("\nHow many extracurriculars did you do in 10th grade: "))

for i in range(num_extra):
    activity = input(f"Enter the name of extracurricular activity {i + 1}: ")
    grade = float(input(f"Enter the grade for {activity} in 10th grade: "))
    extra_curriculars_tenth_grade.append((activity, grade))

# Calculate the extracurricular GPA
extracurricular_grades = [grade for (_, grade) in extra_curriculars_tenth_grade]
extracurricular_gpa = sum(extracurricular_grades) / len(extracurricular_grades)

# Calculate the main GPA for 10th grade
tenth_grade = [tenth_grade_math, tenth_grade_ela, tenth_grade_history, tenth_grade_science]
tenth_grade_gpa = (sum(tenth_grade) + extracurricular_gpa) / (len(tenth_grade) + 1)

print(f"\nYour 10th Grade GPA was: {tenth_grade_gpa:.2f}\n")

# 11th grade inputs
eleventh_grade_math = get_valid_grade("What was your grade for Math in 11th grade: ")
eleventh_grade_ela = get_valid_grade("What was your grade for ELA in 11th grade: ")
eleventh_grade_history = get_valid_grade("What was your grade for History in 11th grade: ")
eleventh_grade_science = get_valid_grade("What was your grade for Science in 11th grade: ")

# Collect 11th-grade extracurricular activities and grades
extra_curriculars_eleventh_grade = []
num_extra = int(input("\nHow many extracurriculars did you do in 11th grade: "))

for i in range(num_extra):
    activity = input(f"Enter the name of extracurricular activity {i + 1}: ")
    grade = float(input(f"Enter the grade for {activity} in 11th grade: "))
    extra_curriculars_eleventh_grade.append((activity, grade))

# Calculate the extracurricular GPA
extracurricular_grades = [grade for (_, grade) in extra_curriculars_eleventh_grade]
extracurricular_gpa = sum(extracurricular_grades) / len(extracurricular_grades)

# Calculate the main GPA for 11th grade
eleventh_grade = [eleventh_grade_math, eleventh_grade_ela, eleventh_grade_history, eleventh_grade_science]
eleventh_grade_gpa = (sum(eleventh_grade) + extracurricular_gpa) / (len(eleventh_grade) + 1)

print(f"\nYour 11th Grade GPA was: {eleventh_grade_gpa:.2f}\n")

# 12th grade inputs
twelfth_grade_math = get_valid_grade("What was your grade for Math in 12th grade: ")
twelfth_grade_ela = get_valid_grade("What was your grade for ELA in 12th grade: ")
twelfth_grade_history = get_valid_grade("What was your grade for History in 12th grade: ")
twelfth_grade_science = get_valid_grade("What was your grade for Science in 12th grade: ")

# Collect 12th-grade extracurricular activities and grades
extra_curriculars_twelfth_grade = []
num_extra = int(input("\nHow many extracurriculars did you do in 12th grade: "))

for i in range(num_extra):
    activity = input(f"Enter the name of extracurricular activity {i + 1}: ")
    grade = float(input(f"Enter the grade for {activity} in 12th grade: "))
    extra_curriculars_twelfth_grade.append((activity, grade))

# Calculate the extracurricular GPA
extracurricular_grades = [grade for (_, grade) in extra_curriculars_twelfth_grade]
extracurricular_gpa = sum(extracurricular_grades) / len(extracurricular_grades)

# Calculate the main GPA for 12th grade
twelfth_grade = [twelfth_grade_math, twelfth_grade_ela, twelfth_grade_history, twelfth_grade_science]
twelfth_grade_gpa = (sum(twelfth_grade) + extracurricular_gpa) / (len(twelfth_grade) + 1)

print(f"\nYour 12th Grade GPA was: {twelfth_grade_gpa:.2f}\n")

# Improve/Unimprove calculations
tenth_grade_improve_percentage = (ninth_grade_gpa / tenth_grade_gpa - 1) * 100
eleventh_grade_improve_percentage = (tenth_grade_gpa / eleventh_grade_gpa - 1) * 100
twelfth_grade_improve_percentage = (eleventh_grade_gpa / twelfth_grade_gpa - 1) * 100

if tenth_grade_gpa > ninth_grade_gpa:
    formatted_percentage = "{:.1f}".format(tenth_grade_improve_percentage)
    print(f"You improved your GPA from 9th to 10th grade by {formatted_percentage:.2f}%\n")
elif ninth_grade_gpa == tenth_grade_gpa:
    print("You had no GPA improvement\n")
else:
    formatted_percentage = "{:.1f}".format(-tenth_grade_improve_percentage)
    print(f"You unimproved your GPA by {formatted_percentage:.2f}%\n")

if eleventh_grade_gpa > tenth_grade_gpa:
    formatted_percentage = "{:.1f}".format(eleventh_grade_improve_percentage)
    print(f"You improved your GPA from 10th to 11th grade by {formatted_percentage:.2f}%\n")
elif tenth_grade_gpa == eleventh_grade_gpa:
    print("You had no GPA improvement\n")
else:
    formatted_percentage = "{:.1f}".format(-eleventh_grade_improve_percentage)
    print(f"You unimproved your GPA by {formatted_percentage:.2f}%\n")

if twelfth_grade_gpa > eleventh_grade_gpa:
    formatted_percentage = "{:.1f}".format(twelfth_grade_improve_percentage)
    print(f"You improved your GPA from 11th to 12th grade by {formatted_percentage:.2f}%\n")
elif eleventh_grade_gpa == twelfth_grade_gpa:
    print("You had no GPA improvement\n")
else:
    formatted_percentage = "{:.1f}".format(-twelfth_grade_improve_percentage)
    print(f"You unimproved your GPA by {formatted_percentage:.2f}%\n")
