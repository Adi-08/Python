s = input("Enter the string: ")
count =0
for ch in s.lower():
    if ch in "aeiou":
        count +=1
print(count)