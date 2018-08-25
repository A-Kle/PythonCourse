print("quiz1\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

# write your function here
def population_density(population, land_area):
    return population/land_area



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

print("quiz2\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

def readable_timedelta(days):
    # insert your docstring here
    """Return readable format of timedelta as weeks and days amount from given days"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

print("quiz3\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
   return sum(num_list) / len(num_list)

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)


print("quiz4\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)

print("quiz5\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    i = start
    for element in iterable:
        yield i, element
        i += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

print("quiz6\n---------------------------------------------------------------------\n")
#---------------------------------------------------------------------

    def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable),size):
        yield iterable[i: i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))