"""reducer.py"""
# fill in code

#!/usr/bin/python

import sys

course = None
current_grade = 0
course_count = 0
key = None

 #Create dictionary for the various courses
Earth_Science = {}
History = {}
Mathematics = {}

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    course, grade, name = line.split('\t', 2)
    
    # convert value (currently a string) to int
    try:
        grade = int(grade)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue
    # create conditions for the courses    
    if course == 'Mathematics':
        Mathematics[name] = grade

    elif course == 'Earth Science':
        Earth_Science [name] = grade

    else:
         History [name] = grade
            
# Sort for Mathematics
Mathematics_sort = sorted(Mathematics.items(), key=lambda x: x[1], reverse=True)
Mathematics_Top5 = list(Mathematics_sort)[:5]
print('Top 5 Students in Mathematics = ', Mathematics_Top5)

# Sort for Earth science
Earth_Science_sort = sorted(Earth_Science.items(), key=lambda x: x[1], reverse=True)
Earth_Science_Top5 = list(Earth_Science_sort)[:5]
print('Top 5 Students in Earth Science = ', Earth_Science_Top5)

# Sort for History
History_sort = sorted(History.items(), key=lambda x: x[1], reverse=True)
History_Top5 = list(History_sort)[:5]
print('Top 5 Students in History = ', History_Top5)

