#strip is used to remove spaces
uinput = input("Enter a string: ")
rstring = uinput[::-1]
if uinput == rstring:
    print(f'"{uinput}" is a palindrome.')
else:
    print(f'"{uinput}" is not a palindrome.')
