# A student makes honour roll if their average is >= 85
# and their lowest grade is not below 75

gpa = float(input('What was your grade point average? '))
lowestGrade = float(input('What was your lowest grade? '))

# if gpa >= 85 and lowestGrade >= 75:
#     print('You made the honour roll')

honorRoll = gpa >= 85 and lowestGrade >= 75

if honorRoll:
    print('You made the honour roll')
else:
    print('You not made the honour roll')
