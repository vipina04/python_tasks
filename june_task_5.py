n = int(input("Enter a number : "))
if n == 1 or n == 0:
    print("Not prime")
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        break
    else:
        print("Its a prime number")