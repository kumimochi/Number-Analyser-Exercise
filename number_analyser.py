#Number Analyser Exercise
number = int(input("Please enter a number."))
mod = number % 2

if number > 0:
        print('Negative')
else:
        print('It\'s zero.')
              
if mod > 0:
              print('This is an odd number.')
else:
              print('This is an even number.')
