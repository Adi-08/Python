num = int(input("Enter the number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //=10

if reverse == num:
    print("palindrome")
else:
    print("Not Palindrome")