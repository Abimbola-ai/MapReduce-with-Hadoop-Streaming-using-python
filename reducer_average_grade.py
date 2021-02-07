"""reducer.py"""
# fill in code
import sys

course_grade = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    course, grade, name = line.split('\t')

    try:
        grade = int(grade)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue
    if course in course_grade:
        course_grade[course].append(int(grade))
    else:
        course_grade[course] = []
        course_grade[course].append(int(grade))   
#Reducer
for course in course_grade.keys():
        ave_grade = sum(course_grade[course])*1.0 / len(course_grade[course])
        print ("%s\t%s" % (course, ave_grade))