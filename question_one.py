def calculate_area(radius):
    pie = 3.14
    area = pie * (radius * 2)
    return area

# Testing the function with a radius of 5
radius = 5
area = calculate_area(radius)
print(area)

#sum of natural numbers
def calculate_sum(n):
    if n == 1:  
        return 1
    else:
        return n + calculate_sum(n - 1)

# Testing the function with n=4
n = 4
sum = calculate_sum(n)
print(sum)

#remove element at index 2 and insert value 10 at the end
numbers = [1, 3, 5, 7, 9]
new_numbers = numbers.pop(2)
new_numbers = numbers.append(10)
print(numbers)

#create new list of even numbers
even_numbers = [2,4,6,8,10]
print("New List:")
for x in even_numbers:
    if x % 2 == 0:
        print(x)

#dictionary below update age to 25 and add new key value pair(city,New york)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 25
student_info['city'] = 'New York'
print(type(student_info))
print(student_info)

#create new dict greater than 5
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}
new_dict = {key: value for key, 
            value in original_dict.items() 
            if value > 5}

print(new_dict)
