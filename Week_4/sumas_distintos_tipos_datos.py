# String + String
name = "Kevin"  
last_name = " Cruz"
print(name + last_name)
# Correct

# String + Int
name = "Alonso"
number = 50
print(name + number)
# TypeError: can only concatenate str (not "int") to str

# Int + String
dog = "Spyke"
age = 7
print(dog + age)
# TypeError: can only concatenate str (not "int") to str

# List + List
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print (list1 + list2)
# Correct, it adds the numbers from list number 1 to list number 2 without summing the numbers.

# String + List
my_list = [1,2,3]
my_name = "Kevin"
print(my_list + my_name)
# TypeError: can only concatenate list (not "str") to list

# Float + int
float_1 = 1.5
int_1 = 3
print(float_1 + int_1)
# Correct 

# Bool + Bool
first_bool = True
second_bool = True
print(first_bool + second_bool)
# Correct, the result True and False = 1, the result False + False = 0, the result True + True = 2