import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("Kursusgang_2/school.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_students_table = """
CREATE TABLE IF NOT EXISTS student(
student_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
major TEXT NOT NULL)
"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS course(
course_id INTEGER PRIMARY KEY,
course_name TEXT NOT NULL,
instructor_name TEXT NOT NULL)
"""

create_enrollment_table = """
CREATE TABLE IF NOT EXISTS enrollment(
enrollment_id INTEGER PRIMARY KEY,
course_id INTEGER NOT NULL,
student_id INTEGER NOT NULL,
FOREIGN KEY (course_id) REFERENCES course (course_id),
FOREIGN KEY (student_id) REFERENCES student (student_id),
UNIQUE(course_id, student_id)
)
"""

create_students = """
INSERT INTO 
    student(student_id, name, major)
VALUES
    (1, 'Mark', 'DAKI'),
    (2, 'Jakob', 'Medialogi'),
    (3, 'Karoline', 'DAKI'),
    (4, 'Bertil','Robotteknologi'),
    (5, 'Arni', 'Sociologi')
"""
create_courses = """
INSERT INTO
    course(course_id, course_name, instructor_name)
VALUES
    (1, 'DAKI', 'Andreas'),
    (2, 'Medialodi', 'Kasper'),
    (3, 'Robotteknologi', 'Magnus'),
    (4, 'Sociologi', 'Bent'),
    (5, 'Nanotech og Fysik', 'Niels')
"""

create_enrollment = """
INSERT INTO
    enrollment(course_id, student_id)
VALUES
    (1, 1),  -- Mark er tilmeldt DAKI
    (2, 2),  -- Jakob er tilmeldt Medialogi
    (3, 4),  -- Bertil er tilmeldt Robotteknologi
    (4, 5),  -- Arni er tilmeldt Sociologi
    (1, 3)   -- Karoline er tilmeldt DAKI
"""

execute_query(connection, create_students_table)
execute_query(connection, create_courses_table)
execute_query(connection, create_students)
execute_query(connection, create_courses)
execute_query(connection, create_enrollment_table)
execute_query(connection, create_enrollment)

def get_courses_for_student(connection, student_name):
    query = """
    SELECT c.course_name
    FROM enrollment e
    JOIN course c ON e.course_id = c.course_id
    JOIN student s ON e.student_id = s.student_id
    WHERE s.name = ?
    """
    cursor = connection.cursor()
    cursor.execute(query, (student_name,))
    courses = cursor.fetchall()
    return courses

student_name = "Mark"
courses_for_student = get_courses_for_student(connection, student_name)
print(f"Kurser for {student_name}:")
for course in courses_for_student:
    print(course[0])

def get_students_for_course(connection, course_name):
    query = """
    SELECT s.name
    FROM enrollment e
    JOIN student s ON e.student_id = s.student_id
    JOIN course c ON e.course_id = c.course_id
    WHERE c.course_name = ?
    """
    cursor = connection.cursor()
    cursor.execute(query, (course_name,))
    students = cursor.fetchall()
    return students

course_name = "DAKI"
students_for_course = get_students_for_course(connection, course_name)
print(f"Studerende for kurset {course_name}:")
for students in students_for_course:
    print(students[0])