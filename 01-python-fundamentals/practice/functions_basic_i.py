#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#the output should be 5
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#this should return an error message since number_of_days_in_a_week_silicon_or_triangle_sides() is not defined
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#the output should be 5 (anything written after the first return won't be read/executed by the function)
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#the output should be 5 (anything written after the return 5 won't be read/executed by the function)
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#the output should be 5 and None since the function doesn't return anything
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#the output should be 3 then 5 then an error message because the add function doesn't return anything only print the sum of two variables and we ca,'t add None to None
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#the output should be 25
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#the output should be 100 then 10
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))#the output should be 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#the output should be 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#the output should 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#the output should be 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#the output should be 500 then 500 then 300 then 500
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#the output should be 500 then 500 then 300 then 500
#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#the output should be 500 then 500 then 300 then 300
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#the output should be 1 then 3 then 2
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#the output should be 1 then 3 then 5 then 10