# Given:
colors = ["red", "blue", "green", "yellow", "purple"]
print(len(colors)) # 6
index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1


# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
