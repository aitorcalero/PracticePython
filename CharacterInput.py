import datetime

name = input("What's your name? ")
age = input("What's your age? ")
futureAge = input("I want to know in which year I'll be... ")

print("\nHello "+name+". You're " + age +" years old\n")

def CalculateAge(currentAge, futureAge):
    date = datetime.datetime.now()
    years = futureAge - currentAge
    return date.year + years


year = CalculateAge(int(age),int(futureAge))

print(name + " you'll be 100 yo in " + str(year))