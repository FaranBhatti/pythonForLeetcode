# ============================================================
# Practice Task: Profile Card
# ============================================================
# Create variables for your name, age, city, and a hobby.
#
# 1. Print a formatted string like:
#    Name: Alice | Age: 25 | City: Vancouver | Hobby: climbing
#
# 2. Bonus: do it again using manual string concatenation
#    (convert age to str manually, no f-strings)

name, age, city, hobby = "Alice", 25, "Vancouver", "climbing"

print(f"Name: {name} | Age: {age} | City: {city} | Hobby: {hobby}")

print("Name: " + name + " | Age: " + str(age) + " | City: " + city + " | Hobby: " + hobby)