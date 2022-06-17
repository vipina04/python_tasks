#Python program to find whether a string is Palindrome or not
str = input("Enter a string:")
rev = str[::-1]
print("The reversed string is :  "+rev)
if str==rev:
    print("entered sting is palindrome")
else:
    print("entered string is not Palindrome")

