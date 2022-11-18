# Prints your age in decades
age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10

strDecade = 'decade'
strYear = 'year'

if decades > 1:
    strDecade = 'decades'

if years > 1:
    strYear = 'years'

print("You're " + str(decades) + " " + strDecade +
      " and " + str(years) + " " + strYear + " old")
