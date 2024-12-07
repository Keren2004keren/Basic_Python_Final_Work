# Start
# Ex 1

for i in range(12, 25):
    print(i, end=" ")
print()

# Ex 2
for i in range(7, 32, 2):
    print(i, end=" ")
print()

# Ex 3
for i in range(10, -21, -2):
    print(i, end=" ")
print()

# Ex 4
for i in range(1, 46):
    if i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i, end=" ")
print()


# Ex 5
def sum_array(ar: list) -> int:
    total_sum: int = 0
    for num in ar:
        total_sum += num
    return total_sum


# Ex 6

# 1
def del_prop(array, property_change):
    for student in array:
        if property_change in student:
            del student[property_change]


# 2
def print_students(array):
    for student in array:
        print(", ".join(f"{key}: {value}" for key, value in student.items()))


# 3
def sorted_students(array):
    return sorted(array, key=lambda student: student["age"], reverse=True)


# Ex 7
our_pets = [
    {"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    {"animal_type": "dog",
     "names": ["Spot", "Bowser", "Frankie"]}
]


def type_cat(array):
    for pet in array:
        if pet["animal_type"] == "cat":
            print(pet)


def animal_type(array, a_type):
    for pet in array:
        if pet["animal_type"] == a_type:
            print(pet["names"])


def name_pet(array, name):
    all_names = set()
    for pet in array:
        all_names.update(pet["names"])
    if name not in all_names:
        for pet in array:
            pet["names"].append(name)
    return array


# Ex 8
student = {'name': 'John', 'age': 20, 'hobbies': ['reading', 'games', 'coding'], }


# 1
def print_data(data: dict):
    for key, value in data.items():
        print(f"{key}: {value}")


# 2
def add_hobby(data: dict, hobby):
    if hobby not in data["hobbies"]:
        data["hobbies"].append(hobby)


# 3
add_hobby(student, "running")
print_data(student)


# 4
def del_hobby(data, hobby):
    if hobby in data["hobbies"]:
        data["hobbies"].remove(hobby)
    return data


# 5
del_hobby(student, "games")
print_data(student)

# 6
student["family name"] = "smith"

print_data(student)

# Ex 9
matrix = [[1, 2], [3, 4], [5, 6]]


def print_element(array):
    for arr in array:
        for element in arr:
            print(element, end=" ")


# Ex 10
matrix = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]


def count_zero(array):
    zeros = 0
    for arr in array:
        for element in arr:
            if element == 0:
                zeros += 1
    return zeros


# Ex 11
arr = [4, 2, 34, 4, 1, 12, 1, 4]


def find_dup(array):
    count = {}
    dups = []
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, times in count.items():
        if times > 1:
            dups.append(num)
    return dups


# Ex 12
def reverse_array(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array


# Ex 13
def array_sum(arr1, arr2):
    sum_arr = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            sum_arr.append(arr1[i] + arr2[i])
    return sum_arr


# Ex 14
def palindrome(str1, str2):
    if str1 == str1[::-1]:
        print(True)
    else:
        print(False)
    if str2 == str2[::-1]:
        print(True)
    else:
        print(False)


# Ex 15
counter = 1
while counter < 100:
    print(counter)
    counter *= 2

# Ex 16
counter = 900000
while counter > 50:
    print(counter)
    counter /= 2


# Ex 17
def repeating(arr_str):
    repeats = []
    checked = []
    index = 0
    while index < len(arr_str):
        array_value = arr_str[index]
        if array_value not in checked:
            counts = 0
            inner_index = 0
            while inner_index < len(arr_str):
                if arr_str[inner_index] == array_value:
                    counts += 1
                inner_index += 1
            if counts > 1:
                repeats.append(array_value)
        checked.append(array_value)
        index += 1
    return repeats


# Ex 18
def without_duplicate(array_str):
    no_dup = []
    index = 0
    while index < len(array_str):
        if array_str[index] not in no_dup:
            no_dup.append(array_str[index])
        index += 1
    return no_dup


# Ex 19
def no_pete(arr_name):
    no_dup_pete = []
    index = 0
    while index < len(arr_name):
        if arr_name[index].lower() == "pete":
            index += 1
            continue
        if arr_name[index] not in no_dup_pete:
            no_dup_pete.append(arr_name[index])
        index += 1
    return no_dup_pete


# Ex 20
def index_consecutive(bools):
    index = 0
    while index < len(bools) - 1:
        if bools[index] == bools[index + 1]:
            return index + 1
        index += 1
    return -1


# Ex 21
while True:
    full_name: str = input("Enter your name:")
    if len(full_name.split()) != 2:
        print("Try again, your name needs to be 2 words.")
        full_name: str = input("Enter your name:")
    age: int = int(input("Enter your age:"))
    if age < 0 or age > 100:
        print("Try again,your age needs to be between 0-100.")
        age: int = int(input("Enter your age:"))
    user_email: str = input("Enter your email:")
    if "@" not in user_email.split():
        print("Wrong input, try again.")
        user_email: str = input("Enter your email:")
    print(f"Your info is: \nFull name: {full_name}\nAge: {age}\nEmail: {user_email}")
    break
