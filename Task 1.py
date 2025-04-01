'''
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

n = int(input('Enter a number: '))

if n%2==0:
    print(n,' is even')
elif n%2==1:
    print(n,' is odd')
else:
    print('Invalid input')