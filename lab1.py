
# q1
def check_range(number):
    try:
        number = float(number)  # Attempt to convert input to float
        if 20 <= number <= 50:
            print(f"{number} is in the range of 20 to 50")
        else:
            print(f"{number} is not in the range of 20 to 50")
    except ValueError:
        print("Input is not a valid number")

num = input("Enter a number: ")
check_range(num)
#q2
def rectangle_area(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width should be greater than zero")
        return length * width
    except ValueError:
        raise ValueError("Length and width must be numeric and greater than zero")

length = input("Enter length : ")
width = input("Enter width : ")

try:
    area = rectangle_area(length, width)
    print("Area:", area)
except ValueError as e:
    print(e)


def rectangle_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width should be greater than zero")
        return 2 * (length + width)
    except ValueError:
        raise ValueError("Length and width must be numeric and greater than zero")

length = input("Enter length : ")
width = input("Enter width : ")

try:
    rectangle = rectangle_perimeter(length, width)
    print("rectangle:", rectangle)
except ValueError as e:
    print(e)



#q3
def concat_strings_method1(str1, str2):
    return str1 + " " +str2

def concat_strings_method2(str1, str2):
    return ' '.join([str1, str2])

string1 = "Hello"
string2 = "World"
print("Method 1:", concat_strings_method1(string1, string2))
print("Method 2:", concat_strings_method2(string1, string2))


# #q4
def square_list(lst):
    result = []
    for x in lst:
        result.append(x ** 2)
    return result

numbers = [1, 2, 3, 4, 5]
print(square_list(numbers))


# #q5
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge_dicts(dict1, dict2))


#q6
def merge_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(merge_lists(list1, list2))

#q7
def check_keys(dictionary):
    return all(key in dictionary for key in ('job', 'card_number'))

dict = {"name": "salma", "email": "salma@gmail.com", "age": 25, "job": "developer", "address": "cairo"}
print(check_keys(dict))


#q8
def sum_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    return total

print("Sum of numbers from 1 to 100:", sum_numbers())

#q9
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

num = 77
print(check_even_odd(num))

#q10
def reverse_string(input_string):
    return input_string[::-1]

text = "beautiful salma"
print(reverse_string(text))


#Q11
def palindrome(input_str):
    reversed_str = input_str[::-1]
    return (input_str == reversed_str)

result = palindrome("heelo")
print(result)

#Q12

def remove_even_square_odd(list_number):
    i=0
    while(i<len(list_number)):
        if(list_number[i]%2==0):
            list_number.pop(i)
        else:
            list_number[i]=list_number[i]**2
            i+=1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_even_square_odd(numbers)
print(numbers)
            


#Q13
def prime(number):
    if number <2:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

test_number = 17
result = prime(test_number)
print(f"{test_number} is prime: {result}")


#Q14
def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
    return result
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")



def perform_operations(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num

    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num

    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num

    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)

    return [total_sum, min, max, squared_list]

numbers = [1, 4, 7, 2, 9]
results = perform_operations(numbers)
print("Sum:", results[0])
print("Minimum:", results[1])
print("Maximum:", results[2])
print("Squared List:", results[3])


