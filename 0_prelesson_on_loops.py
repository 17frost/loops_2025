# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
# You can iterate over a range, string, sequence, etc.
for x in reversed(range(1, 11, 3)): # add a 3rd comma, followed by 2 to count by twos, and so on.
    print(x)

print("HAPPY NEW YEAR")

name = input("Enter your name: ")
while name == "":
    print("enter ur damn name bruh")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("how old r u: "))
while age < 0:
    print(f"buddy u cant be {age} years old")
    age = int(input("how old r u: "))
