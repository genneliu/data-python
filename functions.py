# 1
def hello_world():
    print("Hello, World!")

hello_world()

# 2
def print_name(name):
    print(name)

print_name("Genne")

# 3
def greeting(name):
    print("Hello " + name)

greeting("Genne")

#4
def add(num1, num2):
    return num1+ num2

sum = add(5, 7)
print(sum)


#5
def name_check(name):
    if name == "Steven":
        return "What's up Steven?"
    elif name == "Bryan":
        return "Hey, Bryan!"
    else:
        cool_name = "Cool Name " + name
        return cool_name

name_greeting = name_check("Luna")
print(name_greeting)

#6
def fav_color_finder(color):
    if color == "red":
        return "red is a great color"
    elif color == "green":
        return "green is the best color"
    elif color == "black":
        return "you're so trendy"
    else:
        return "you need to re-evaluate your color choice"

color_rating = fav_color_finder("green")
print(color_rating)

#7 

def print_all_names(names):
    for i in names:
        print(i)

names = print_all_names(["Jacob", "Luna", "Genne"])


#8
def thats_odd(num):
    if num % 2 == 0:
        return "that's not odd!"
    else:
        return "That is odd indeed"

odd_checker = thats_odd(9)
print(odd_checker)


#9
list = [2, 5, 34, 678, 2, 225, 976]


def big_or_small(nums):
    answers = []
    for i in nums:
        if i <= 100:
            answers.append("small")
        elif i >= 100:
            answers.append("big")
    return answers

big_or_small_results = big_or_small(list)
print(big_or_small_results)

#10
contestants = ['Katniss', 'Peeta', 'Fox-face', 'Glimmer', 'Cato', 'Rue', 'Thresh', 'Clove', 'Marvel']
loser = 'Glimmer'

def the_eliminator(cont, loser):
    for i in cont:
        if i == loser:
            cont.pop(i)
    return cont



new_contestants = the_eliminator(contestants, loser)
print(new_contestants)

#11
def upper_case(yell):
    print(yell.upper())

yell_this = upper_case("luna is a good dog")
print(yell_this)

