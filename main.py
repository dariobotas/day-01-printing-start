# Write your code below this line 👇
#print("Hello World!")

##fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
#vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

#dirty_dozen = [fruits, vegetables]

#print(dirty_dozen[1][1])


#Write your code below this row 👇
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
