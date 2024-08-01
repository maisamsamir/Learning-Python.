#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")

# ax = "joe"
#az = "60"
#print("hello my name is "  + ax +"")
#print("my age is " + az +"")

#ax = "james"
#az = " 40"
#print("i like the name " + ax +"")
#print("but i dont like being " + az + "")

# print("HELLO\"world")
# print("hello\nworld")

#q1 = "hello how "
#print(q1 + "are you")
#print(q1.upper().isupper())
# print(len(q1)) how many characters
#print(q1[0])
#print(q1.index("how"))
#print(q1.replace("how", "can"))
 
#print(-2.0987)
#print( 32522352 + 32582852)
#print(4 *4 -6+9)
#print(20 / 10)
#num=-58
#print(num)
#print(str(num )+ " my fav num")
#print(abs(num)) 
#print(pow(3,3))
#print(max(4,6))
#print(min(4,6))
#print(round(17411.3))

#from math import *
#print(floor(3.7))
#print(ceil(4.1))
#print(sqrt(144))
#name = input("enter your name: ")
#age = input("enter your age: ")
#print("hello " + name + "! " + "You are " + age + "!")
# CALCULATOR 1
#num1 = input("Enter a number: ")
#num2 = input("Enter a second number: ")
#result = float(num1)  + float(num2)
#print(result)
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrit: ")
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("i love " + celebrity)

#lucky_numbers = [4,8,12,16,20]
#friends = ["Kevin", "Karen", "Jim", "toby", "todd"]
#friends2 = friends.copy()
#print(friends2)
#friends.reverse()
#friends.sort()
#print(friends)
#print(friends.count("Jim"))
#print(friends.index("Kevin"))
#friends.pop()
#friends.clear()
#friends.remove("Jim")
#friends.insert(1,"Kelly")
#friends.append("creed")
#friends.extend(lucky_numbers)
#print(friends)
#friends[1] = "Mike"
#print(friends[1:3])

#coordinates = [(4,5), (6,7), (80, 95)]
#print(coordinates[1])

#def sayhi(name, age):
    #print("Hello " + name +", You are " + str(age))
#print("Top")
#print("Bottom")
#sayhi("Mike", 35)
#sayhi("Steve", 30)

#def cube(num):
 #num*num*num
#result = cube(4)
#print(result)    

#is_male = False
#is_tall = True
#if is_male or is_tall:
#if is_male and is_tall:
   #print("You are a tall male")
#elif not(is_male) and is_tall:
    #print("You are not a male but are tall")
#elif is_male and not(is_tall):
    #print("You are a male but not tall")
#else:     
    #print("You are not a male and short")

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
      #  return num1
    #elif num2 >= num1 and num2 >= num3:
     #   return num2 
    #else:
       # return num3
    #print(max_num(3,40,5))

#num1 = float(input("ENTER FIRST NUMBER: "))
# operator = input("ENTER AN OPERATOR")
# num2 = float(input("ENTER SECOND NUMBER: "))
#if operator == "+":
   # print(num1 + num2)
#elif operator == "-":
   # print(num1 - num2)
#elif operator == "/":
   # print(num1 / num2)
#elif operator == "*":
  #  print(num1*num2)
#else:
    #print("Use one of the following opereators only: +, -, *, /")

#monthconversions = {
 #   "Jan":"January",
  #  "Feb":"Febuary",
   # "Mar":"March",
   # "Apr":"April",
   # "May":"May",
    #"Jun":"June",
  #  "Jul":"July",
   # "Aug":"August",
  #  "Sep":"September",
  #  "Oct":"October",
   # "Nov":"November",
   # "Dec":"December",}
#print(monthconversions["Jan"])

#i=1
#while i <= 10:
 #   print(i)
  #  i += 1
#print("done w loop")

#secret_word = "rat"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False
#while guess != secret_word and not(out_of_guesses):
 #if guess_count < guess_limit:
      #  guess = input("Enter guess: ")
       # guess_count += 1
 #else: 
  #  out_of_guesses = True
#if out_of_guesses:
 # print("You lose!")
#else: 
 #  print("You win")
  
#for letter in "elephant":
  #  print(letter)
#friends = ["Jim","Karen","Martha"]
#for index in range(len(friends)):
  #  print(friends[index])

#print(2**3)
#def raise_to_power(base_num, pow_num):
   # result = 1
   # for index in range(pow_num):
      #  result = result*base_num
  #  return result
#print(raise_to_power(3,5))

#number_grid = [
 #   [1,2,3],
  #  [4,5,6],
   # [7,8,9],
    #[0]]
#print(number_grid[2][1])
#for row in number_grid:
 #   for col in row:
      #  print(col)

#def translate(phrase):
   ## transalation = ""
    ##for letter in phrase:
       # if letter in "AIEOUaeiou":
          #  transalation = transalation + "g"
       # else:
            #transalation = transalation + letter
    #return transalation
#print(translate(input("Enter a Phrase. ")))
 
#try: 
 #value = 10/0
 #number = int(input("Enter a number: "))
 #print(number)
#except ValueError:
 #print("Invalid Input")
#except ZeroDivisionError:
 #print("Zero Division Error")

#class student:
    #def __init__(self, name, major, gpa, is_on_probation):
       # self.name = name
        #self.major = major
        #self.gpa = gpa
        #self.is_on_probation = is_on_probation

#from Test import Question
#question_prompt = [
   # "What colour are apples?\n (a) Red/Green\n (b) Purple\n (c) Orange\n\n",
    #"What colour are Bananas\n (a) Teal\n (b) Yellow\n (c) Pink\n\n",
    #"What colour are strawberries\n (a) Yellow\n (b) Blue\n (c) Red\n\n"
#]
#questions = [
   # Question(question_prompt[0], "a"),
   # Question(question_prompt[1], "b"),
    #Question(question_prompt[2], "c"), 
    #]

#def run_test(questions):
   # score = 0
    #for question in questions:
       # answer = input(question.prompt)
        #if answer == question.answer:
           # score += 1
    #print("You got " + str(score) + "/" + str(len(questions))+ " Correct")

#  run_test(questions)

# from Student import Student
# student1 = Student("Jim","Business", 3.7)
# student2 = Student("Tim","Art", 2.9)
# print(student1.on_honor_roll())

# from Student import chef
# from chinchef import ChineseChef
# mychef = chef()
# mychef.make_special_dish()

# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()

# main_script.py


# num1 = float(input("Enter your first number: "))
# op = input("Select your operator: ")
# num2 = float(input("Enter your second number: "))
# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1/num2)
# elif op == "^":
#     print(num1**num2)

