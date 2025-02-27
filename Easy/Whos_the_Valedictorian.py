grade_points = { 
    'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0
}

cases = int(input().rstrip())

for i in range(cases):
    school_name = input().strip()
    num_students = int(input().strip())
    
    top_student = ""
    highest_gpa = -1
    highest_total_credits = -1
    
    for _ in range(num_students):
        student_info = input().strip().split(":")
        student_name = student_info[0]
        courses = student_info[1].split(",")
        
        total_grade = 0
        total_credits = 0
        
        for course in courses:
            grade = course[0]
            credit = int(course[1:])
            
            total_grade += grade_points[grade] * credit
            total_credits += credit

        if total_credits > 0:
            gpa = total_grade / total_credits

            if gpa > highest_gpa or (gpa == highest_gpa and total_credits > highest_total_credits):
                highest_gpa = gpa
                highest_total_credits = total_credits
                top_student = student_name
    
    if top_student:
        print(f"{school_name} = {top_student}")
