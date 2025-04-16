from datetime import datetime

students_db = []
admins_db = {}

def add_student(name, number, code):
    students_db.append({
        "name": name,
        "number": number,
        "code": code,
        "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def get_all_students(student_name=None, grade=None, level=None):
    filtered_students = students_db
    if student_name:
        filtered_students = [student for student in filtered_students if student_name.lower() in student['name'].lower()]
    if grade:
        filtered_students = [student for student in filtered_students if student.get('grade') == grade]
    if level:
        filtered_students = [student for student in filtered_students if student.get('level') == level]
    return filtered_students

def add_admin_info(username, password):
    admins_db[username] = password
