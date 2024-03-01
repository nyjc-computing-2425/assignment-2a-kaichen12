num = input('Enter a number (decimal or integer): ')
# type your code here
num1 = num.strip(' ')
num2 = num1.replace('.' , '')
num3 = num2.lstrip('0')
sf = len(num3)
# sanitise the input
#take away spaces before after the input
#strip method  tool be using  .strip()
#remove the dot  replace
# .lstrip()
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
