#1
hours_in_a_year = 1 * 365 * 24
print(hours_in_a_year)

minutes_in_a_decade = 10 * 365 * 24 * 60
print(minutes_in_a_decade)

seconds_old_in_year = 24 * 365 * 24 * 60 * 60
print(seconds_old_in_year)

#2
age = 1406000000 / 60 / 60 / 24 / 365
print(round(age))

#3
def compare(a ,b):
  result = [0,0];
  for i in range(0, 3):
    if(a[i] > b[i]):
       result[0] += 1
    elif(a[i] < b[i]):
       result[1] += 1
  
  return result


print('Compare result:', compare([1, 5, 4], [1, 5, 8]))
  

#4
star = "* "
rowCount = 7

for i in range(rowCount, 0, -1):
    starCount = star * rowCount
    print(starCount)
    rowCount -= 1

#5
def triangle_area(b, h):
    return 0.5 * b * h

print(triangle_area(2.28, 3.55))